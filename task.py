import threading
import time
import inspect
import ctypes

def _async_raise(tid, exctype):
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

class Task(threading.Thread):
	def __init__(self,*args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		super(Task, self).__init__(*self.args, **self.kwargs)

	def start(self):
		if self.isAlive():
			print(self.name,'任务已经在执行!')
		else:
			self.__init__(*self.args, **self.kwargs)
			print(self.name,'开始执行!',self.name)
			super().start()
			# self.status = 'running'

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
		_async_raise(self.get_my_tid(), exctype)

	def stop(self):
		"""raises SystemExit in the context of the given thread, which should
		cause the thread to exit silently (unless caught)"""
		if self._is_stopped:
			print(self.name, '任务已经停止!')
		else:
			print(self.name,'任务停止!')
			self.raise_exc(SystemExit)
			self._is_stopped = True

	@property
	def status(self):
		if self.isAlive():
			return 'running'
		else:
			return 'stopped'

# def fun1():
#     for i in range(10):
#         print(i)
#         time.sleep(1)
#
# t1 = Task(name='t1', target=fun1)
# # t1.stop()
# # time.sleep(2)
# t1.start()
# time.sleep(1)
# t1.stop()
# time.sleep(1)
# t1.start()

