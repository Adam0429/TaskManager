import threading
import time
import inspect
import ctypes


class Task(threading.Thread):
	def __init__(self,*args, **kwargs):
		self.args = args
		if 'file' in kwargs:
			exec(f"from task_code import {(kwargs['file'].replace('.py', ''))}")
			print(f"from task_code import {(kwargs['file'].replace('.py', ''))}")
			kwargs['target'] = eval(f"{kwargs['file'].replace('.py', '')}.{kwargs['target']}")
			del kwargs['file']
		print(kwargs)
		self.kwargs = kwargs
		super(Task, self).__init__(*self.args, **self.kwargs)

	def start(self):
		if self.isAlive():
			print(self.name,'任务已经在执行!')
		else:
			# 一个线程只能运行一次，下一次需要初始化
			self.__init__(*self.args, **self.kwargs)
			print(self.name,'开始执行!',self.name)
			super().start()
			# self.status = 'running'

	def restart(self):
		self.stop()
		self.start()

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

# def fun1():
#     for i in range(3):
#         print(i)
#         time.sleep(1)
#
# def fun2():
#     for i in range(10):
#         print(i+100)
#         time.sleep(1)

t1 = Task(name='t1', target='fun1', file = 'f2.py')
# t2 = Task(name='t2', target=fun2)

t1.start()
# time.sleep(2)
#
# t1.restart()


