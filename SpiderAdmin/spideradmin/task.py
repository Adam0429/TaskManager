import threading
import time
import inspect
import ctypes
import traceback
import sys
import inspect
import datetime
import re
import random
from schedule import Job

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
		print(kwargs['name'])
		kwargs['name'] = kwargs['name'].split('/')[kwargs['name'].count('/')].replace('.py','')
		if 'file' in kwargs:
			print(f"from {(kwargs['file'].replace('.py', '')).replace('/', '.')} import *")
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
		self.if_loop = False #默认是非重复任务
		# self.log = ''
		super(Task, self).__init__(*self.args, **self.kwargs)

	def run(self):
		try:
			# super().run()
			# if self._target:
			# 	job = Job(interval=1)
			# 	job.job_func = self._target
			# 	job.unit = 'seconds'
			# 	job.do(self._target)
			if self.if_loop: #定时任务
				while True:
					if self.next_run == None or datetime.datetime.now() > self.next_run:
						if self.next_run == None:
							self.next_run = datetime.datetime.now()
						self._target(*self._args, **self._kwargs)
						self._schedule_next_run()
						self.success = True
					time.sleep(1)
			else:
				self._target(*self._args, **self._kwargs)
				self.success = True

		except Exception as e:
			self.exception = e
			self.success = False
			self.exc_traceback = ''.join(traceback.format_exception(*sys.exc_info()))

	def start(self,args=()):
		if self.isAlive():
			print(self.name,'任务已经在执行!')
		else:
			# 一个线程只能运行一次，下一次需要初始化
			self.kwargs['args'] = args
			self.__init__(*self.args, **self.kwargs)
			print(self.name,'开始执行!',self.name)
			super().start()
			# self.status = 'running'

	def restart(self,args=()):
		self.stop()
		self.start(args=self.kwargs['args'])

	def stop(self):
		"""raises SystemExit in the context of the given thread, which should
		cause the thread to exit silently (unless caught)"""
		if self.isAlive() == False:
			print(self.name, '任务已经停止!')
		else:
			print(self.name,'任务停止!')
			self.raise_exc(SystemExit)
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

	def set_loop(self,unit,interval=1,start_time=None):
		self.unit = unit
		self.interval = interval
		self.if_loop = True
		self.next_run = None
		self.start_time = start_time
		self._schedule_next_run()

	def _schedule_next_run(self):
		if self.unit not in ['seconds', 'minutes', 'hours', 'days', 'weeks']+list(weekdays):
			raise Exception('Invalid unit')

		if self.next_run == None: #第一次计算下次运行时间
			now = datetime.datetime.now()
			weekday_dates = {}
			today = datetime.date.today()
			idx = (today.weekday() + 1) % 7
			for idx in range(7):
				t = today + datetime.timedelta(idx)
				weekday_dates[t.weekday()] = today + datetime.timedelta(idx)

			if self.start_time != None:  # 指定开始时间
				time_values = [int(v) for v in self.start_time.split(':')]
				if len(time_values) == 3:
					hour, minute, second = time_values
				elif len(time_values) == 2 and self.unit == 'minutes':
					hour, minute = time_values
					second = 0
				if self.unit not in weekdays:
					self.next_run = datetime.datetime(now.year, now.month, now.day, hour, minute, second)
				else:
					next_run_day = weekday_dates[weekdays.index(self.unit)]
					self.next_run = datetime.datetime(next_run_day.year, next_run_day.month, next_run_day.day, hour, minute,second)
				if datetime.datetime.now() > self.next_run: #如果指定时间早于当前时间，需要特殊处理。将下次执行时间移到晚于当前
					if self.unit in weekdays:
						self.period = datetime.timedelta(**{'days': 7})
					else:
						self.period = datetime.timedelta(**{self.unit: self.interval})
					if self.unit in ['seconds', 'minutes', 'hours']:
						self.next_run = datetime.datetime.now() + self.period
					else:  # 避免多次运行后，任务运行时间延后
						self.next_run = self.next_run + self.period
			else:#没有指定开始时间，则默认为现在
				if self.unit not in weekdays:
					self.next_run = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
				else:
					next_run_day = weekday_dates[weekdays.index(self.unit)]
					self.next_run = datetime.datetime(next_run_day.year, next_run_day.month, next_run_day.day, now.hour,now.minute, now.second)

		else:#非第一次计算下次运行时间
			if self.unit in weekdays:
				self.period = datetime.timedelta(**{'days': 7})
			else:
				self.period = datetime.timedelta(**{self.unit: self.interval})
			if self.unit in ['seconds', 'minutes','hours']:
				self.next_run = datetime.datetime.now() + self.period
			else:# 避免多次运行后，任务运行时间延后
				self.next_run = self.next_run + self.period
		print('下次运行时间:',self.next_run)
		# if self.start_day is not None:
		# 	if self.unit != 'weeks':
		# 		raise Exception('`unit` should be \'weeks\'')
		# 	weekdays = (
		# 		'monday',
		# 		'tuesday',
		# 		'wednesday',
		# 		'thursday',
		# 		'friday',
		# 		'saturday',
		# 		'sunday'
		# 	)
		# 	if self.start_day not in weekdays:
		# 		raise Exception('Invalid start day')
		# 	weekday = weekdays.index(self.start_day)
		# 	days_ahead = weekday - self.next_run.weekday()
		# 	if days_ahead <= 0:  # Target day already happened this week
		# 		days_ahead += 7
		# 	self.next_run += datetime.timedelta(days_ahead) - self.period
		# if self.at_time is not None:
		# 	if (self.unit not in ('days', 'hours', 'minutes')
		# 			and self.start_day is None):
		# 		raise Exception(('Invalid unit without'
		# 								  ' specifying start day'))
		# 	kwargs = {
		# 		'second': self.at_time.second,
		# 		'microsecond': 0
		# 	}
		# 	if self.unit == 'days' or self.start_day is not None:
		# 		kwargs['hour'] = self.at_time.hour
		# 	if self.unit in ['days', 'hours'] or self.start_day is not None:
		# 		kwargs['minute'] = self.at_time.minute
		# 	self.next_run = self.next_run.replace(**kwargs)
		# 	# Make sure we run at the specified time *today* (or *this hour*)
		# 	# as well. This accounts for when a job takes so long it finished
		# 	# in the next period.
		# 	if not self.last_run \
		# 			or (self.next_run - self.last_run) > self.period:
		# 		now = datetime.datetime.now()
		# 		if (self.unit == 'days' and self.at_time > now.time() and
		# 				self.interval == 1):
		# 			self.next_run = self.next_run - datetime.timedelta(days=1)
		# 		elif self.unit == 'hours' \
		# 				and (
		# 				self.at_time.minute > now.minute
		# 				or (self.at_time.minute == now.minute
		# 					and self.at_time.second > now.second)
		# 		):
		# 			self.next_run = self.next_run - datetime.timedelta(hours=1)
		# 		elif self.unit == 'minutes' \
		# 				and self.at_time.second > now.second:
		# 			self.next_run = self.next_run - \
		# 							datetime.timedelta(minutes=1)
		# if self.start_day is not None and self.at_time is not None:
		# 	# Let's see if we will still make that time we specified today
		# 	if (self.next_run - datetime.datetime.now()).days >= 7:
		# 		self.next_run -= self.period
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
#
# t1.restart()


