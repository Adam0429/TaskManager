import time
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
def run():
	"""这里是f2函数"""
	for i in range(100):
		if i == 5:
			raise Exception('错误1！！')
		time.sleep(1)