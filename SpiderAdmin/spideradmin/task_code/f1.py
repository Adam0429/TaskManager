import time
def run():
	for i in range(100):
		if i == 2:
			raise Exception('错误1！！')
		time.sleep(1)