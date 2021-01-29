import time
def run():
	"""这里是f2函数"""

	for i in range(100):
		if i == 2:
			raise Exception('错误1！！')
		time.sleep(1)