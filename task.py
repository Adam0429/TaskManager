import threading
import time
import ctypes
import traceback
import sys
import inspect
import datetime
import re
from schedule import Job
import _thread
import random
from producer import Producer

weekdays = (
	'monday',
	'tuesday',
	'wednesday',
	'thursday',
	'friday',
	'saturday',
	'sunday'
)

class Task(threading.Thread):
	def __init__(self,*args, **kwargs):
		# print(kwargs['name'])
		kwargs['name'] = kwargs['name'].split('/')[kwargs['name'].count('/')].replace('.py','')
		if 'file' in kwargs:
			# print(f"from {(kwargs['file'].replace('.py', '')).replace('/', '.')} import *")
			exec(f"from {(kwargs['file'].replace('.py', '')).replace('/','.')} import *")
			if 'target' not in kwargs:
				kwargs['target'] = eval(f"run")
			else:
				kwargs['target'] = eval(f"{kwargs['file'].replace('.py', '')}.{kwargs['target']}")
			del kwargs['file']
		if not callable(kwargs['target']):
			raise TypeError("the function must be callable")
		self.doc = kwargs['target'].__doc__
		self.params = inspect.getargspec(kwargs['target']).args
		# for param in self.params:
		# 	kwargs[param] = 1
		# 	print(param)
		self.args = args
		self.kwargs = kwargs
		self.success = None
		self.exception = None
		self.exc_traceback = ''
		self.if_loop = False
		self.if_notify = True  #可以改成level,按照warn,error,info处理
		# self.log = ''
		super().__init__(*self.args, **self.kwargs)
		self.init_producer()

	def run(self):
		if self.if_loop:  # 定时任务
			while True:
				self._is_stopped = False
				if datetime.datetime.now() > self.next_run:
					try:
						self.producer.publish('TaskManager:log',self.name+' run')
						self._target(*self._args, **self._kwargs)
						self.success = True
						self.exc_traceback = ''
					except Exception as e:
						self.exception = e
						self.success = False
						self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))
						self.producer.publish('TaskManager:log', self.name + ' failed ' + self.exc_traceback)
						if self.if_notify:
							self.producer.publish('TaskManager:send_email', self.exc_traceback)
					finally:
						self._schedule_next_run()
						time.sleep(1)

		else:
			self._is_stopped = False
			try:
				self.producer.publish('TaskManager:log', self.name + ' run')
				self._target(*self._args, **self._kwargs)
				self.success = True

			except Exception as e:
				self.exception = e
				self.success = False
				self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))
				self.producer.publish('TaskManager:log', self.name + ' failed ' + self.exc_traceback)
				if self.if_notify:
					self.producer.publish('TaskManager:send_email', self.exc_traceback)

	def start(self,args=()):
		if self.isAlive():
			print(self.name,'任务已经在执行!')
		else:
			# 一个线程只能运行一次，下一次需要初始化(改写了)
			# self.kwargs['args'] = args
			# self.__init__(*self.args, **self.kwargs)
			self.start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			print(self.name,'开始执行!')
			self._started._flag = False
			super().start()


	def restart(self,args=()):
		self.stop()
		self.start(args=self.kwargs['args'])

	def stop(self):
		"""raises SystemExit in the context of the given thread, which should
		cause the thread to exit silently (unless caught)"""
		if self.isAlive() == False:
			print(self.name, '停止失败！cause:任务已经停止')
			self.producer.publish('TaskManager:log', self.name + ' stop failed')
		else:
			print(self.name,'任务停止成功!')
			self.raise_exc(SystemExit)
			self.producer.publish('TaskManager:log', self.name + ' stop succeed')
			time.sleep(1)
			# """" 如果不用sleep函数，restart()会提示：任务已经在执行。因为是stop函数没有执行完成，上一个线程还没有被杀死"""
			# self._is_stopped = True

	def async_raise(self, tid, exctype):
		"""raises the exception, performs cleanup if needed"""
		tid = ctypes.c_long(tid)
		if not inspect.isclass(exctype):
			exctype = type(exctype)
		res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
		if res == 0:
			raise ValueError("invalid thread id")
		elif res != 1:
			# """if it returns a number greater than one, you're in trouble,
			# and you should call it again with exc=NULL to revert the effect"""
			ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
			raise SystemError("PyThreadState_SetAsyncExc failed")

	def get_my_tid(self):
		"""determines this (self's) thread id"""
		if not self.isAlive():
			raise threading.ThreadError("the thread is not active")
		# do we have it cached?
		if hasattr(self, "_thread_id"):
			return self._thread_id
		# no, look for it in the _active dict
		for tid, tobj in threading._active.items():
			if tobj is self:
				self._thread_id = tid
				return tid
		raise AssertionError("could not determine the thread's id")

	def raise_exc(self, exctype):
		"""raises the given exception type in the context of this thread"""
		self.async_raise(self.get_my_tid(), exctype)

	@property
	def status(self):
		if self.isAlive():
			return 'running'
		else:
			return 'stopped'

	@property
	def info(self):
		return {'status':self.status,'success':self.success,'doc':self.doc,'exception':self.exception,'exc_traceback':self.exc_traceback}

	@property
	def all_info(self):
		return self.__dict__

	def set_loop(self,unit,interval,loop_start_time=None):
		'''
		:param unit: 如果unit值为指定的星期(1-7),开始时间的日期为下一个最近的这个日子。如果unit为['seconds', 'minutes', 'hours', 'days'],则开始时间的日期为今日
		:param interval: unit的数量，当unit值为指定的星期(1-7)时，此参数没有用
		:param loop_time: 循环开始的时间（不包含日期）如 10:00:00
		:return:
		'''
		self.unit = unit
		self.interval = interval
		self.if_loop = True
		self.next_run = None
		self.loop_start_time = loop_start_time
		self._schedule_next_run()


	def _schedule_next_run(self):
		if self.unit not in ['seconds', 'minutes', 'hours', 'days']+list(weekdays):
			raise Exception('Invalid unit')

		if self.unit in weekdays:
			self.period = datetime.timedelta(**{'days': 7})
		else:
			self.period = datetime.timedelta(**{self.unit: self.interval})

		if self.next_run == None: #第一次计算下次运行时间
			now = datetime.datetime.now()
			weekday_dates = {}
			today = datetime.date.today()
			idx = (today.weekday() + 1) % 7
			for idx in range(7):
				t = today + datetime.timedelta(idx)
				weekday_dates[t.weekday()] = today + datetime.timedelta(idx)

			# if self.loop_time != None:  # 指定开始时间
			time_values = [int(v) for v in self.loop_start_time.split(':')]
			if len(time_values) == 3:
				hour, minute, second = time_values
			else:
				raise Exception("start_time format is invalid!")

			self.loop_start_time = datetime.datetime.now().strftime('%Y-%m-%d') + ' ' + self.loop_start_time
			if self.unit not in weekdays:
				self.next_run = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
			else:
				next_run_day = weekday_dates[weekdays.index(self.unit)]
				self.next_run = datetime.datetime(next_run_day.year, next_run_day.month, next_run_day.day, hour, minute,second)
			# if datetime.datetime.now() > self.next_run: #如果指定时间早于当前时间，需要特殊处理。将下次执行时间移到晚于当前
			# 	if self.unit in weekdays:
			# 		self.period = datetime.timedelta(**{'days': 7})
			# 	else:
			# 		self.period = datetime.timedelta(**{self.unit: self.interval})
			# 	if self.unit in ['seconds', 'minutes', 'hours']:
			# 		self.next_run = datetime.datetime.now() + self.period
			# 	else:  # 避免多次运行后，任务运行时间延后
			# 		self.next_run = self.next_run + self.period
			# else:#没有指定开始时间，则默认为现在
			# 	if self.unit not in weekdays:
			# 		self.next_run = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
			# 	else:
			# 		next_run_day = weekday_dates[weekdays.index(self.unit)]
			# 		self.next_run = datetime.datetime(next_run_day.year, next_run_day.month, next_run_day.day, now.hour,now.minute, now.second)
			# 	self.loop_time = self.next_run
		else:#非第一次计算下次运行时间
			if self.unit in ['seconds', 'minutes','hours']:
				self.next_run = datetime.datetime.now() + self.period
			else:# 避免多次运行后，任务运行时间延后
				self.next_run = self.next_run + self.period
		self.next_run = datetime.datetime(self.next_run.year, self.next_run.month, self.next_run.day, self.next_run.hour, self.next_run.minute, self.next_run.second)
		print('下次运行时间:',self.next_run)

	def init_producer(self):
		# generate client ID with pub prefix randomly
		self.producer = Producer('producer-'+self.name)


# import time
# def fun1(a):
#     for i in range(10):
#         """这里是f2函数"""
#         time.sleep(1)
#         print('f2',i)

#
# def fun2():
#     for i in range(10):
#         print(i+100)
#         time.sleep(1)

# t1 = Task(name='t1', target=fun1,args=(1,))
# t2 = Task(name='t2', target='fun1', file = 'f1.py')
#
# t1.start()
# t2.start()
# time.sleep(2)
# t1.restart()


