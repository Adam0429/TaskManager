import threading
import time
import inspect
import ctypes
import traceback
import sys
import inspect


class Task(threading.Thread):
	def __init__(self,*args, **kwargs):
		kwargs['name'] = kwargs['name'].split('/')[kwargs['name'].count('/')].replace('.py','')
		if 'file' in kwargs:
			# print(f"from {(kwargs['file'].replace('.py', '')).replace('/', '.')} import *")
			exec(f"from {(kwargs['file'].replace('.py', '')).replace('/','.')} import *")
			if 'target' not in kwargs:
				kwargs['target'] = eval(f"run")
			else:
				kwargs['target'] = eval(f"{kwargs['file'].replace('.py', '')}.{kwargs['target']}")
			del kwargs['file']
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
		self.start_args = ()
		# self.log = ''
		super(Task, self).__init__(*self.args, **self.kwargs)

	def run(self):
		try:
			super().run()
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
		self.start(args=self.start_args)

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


