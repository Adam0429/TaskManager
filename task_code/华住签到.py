import time
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime
from retrying import retry

requests.packages.urllib3.disable_warnings()


def email(subject='华住积分签到程序',text=''):
	from_addr = '872490934@qq.com'
	password = 'ultyrlpfwaqdbddd'
	# 输入SMTP服务器地址:
	smtp_server = 'smtp.qq.com'
	# 输入收件人地址:

	server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
	# server.set_debuglevel(1)  这是输出日志

	sender = '872490934@qq.com'
	receivers = ['872490934@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	
	message = MIMEText(text, 'plain', 'utf-8')

	message['From'] = Header(subject, 'utf-8')   # 发送者
	message['To'] =  Header("", 'utf-8')        # 接收者
	
	message['Subject'] = Header(subject, 'utf-8')

	server.login(from_addr, password)
	server.sendmail(from_addr, receivers, message.as_string())
	server.quit()


# @retry(stop_max_attempt_number=10,wait_random_min=30000,wait_random_max=30000)
def signIn():
	print('正在签到...')
	headers = {
	    'Host': 'newactivity.huazhu.com',
	    'Origin': 'https://campaign.huazhu.com',
	    'fp': '23f880ff-87c9-4d79-87a6-5d7a50793701',
	    'Accept': 'application/json, text/plain, */*',
	    'User-Agent': 'HUAZHU/ios/iPhone10,2/13.6/7.91.4/HUAZHU/ios/iPhone10,2/13.6/7.91.4/HUAZHU/ios/iPhone10,2/13.6/7.91.4/HUAZHU/ios/iPhone10,2/13.6/7.91.4/HUAZHU/ios/iPhone10,2/13.6/7.91.4/Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
	    'Referer': 'https://campaign.huazhu.com/pointsShop/?APP_NeedLoginInfo=True&has_video=true&type=',
	    'Accept-Language': 'zh-cn',
	}

	data = {
	  'day': str(datetime.now().day),
	  'state': '0',
	  'channel': 'APP',
	  'source': 'APP',
	  'sk': 'cfe53a2265834b81b3b3ce4ca79f5920069615093'
	}
	response = requests.post('https://newactivity.huazhu.com/v1/pointStore/signIn', headers=headers, data=data,verify=False)
	if response.json()['data']['success']:
		print(f"签到成功！获得积分{str(response.json()['data']['point'])}")
		# email(subject=f"{datetime.now().date()}签到成功！获得积分{str(response.json()['data']['point'])}")
	else:
		print(f"签到失败！{response.text}")
		raise Exception("抛出一个异常")
		# email(text=f"{datetime.now().date()}签到失败！{response.text}")

def run():
	print(datetime.now().date())
	signIn()

	# finally:
	# 	time.sleep(60*60*24)

if __name__ == '__main__':
	run()
# 抽奖
# headers = {
#  'Host': 'newactivity.huazhu.com',
#  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#  'Origin': 'https://campaign.huazhu.com',
#  'Accept': '*/*',
#  'User-Agent': 'HUAZHU/ios/iPhone10,2/13.6/7.91.4/HUAZHU/ios/iPhone10,2/13.6/7.91.4/HUAZHU/ios/iPhone10,2/13.6/7.91.4/Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
#  'Referer': 'https://campaign.huazhu.com/NewWheel/NewWheel.html?objectClass=PONYNEW',
#  'Accept-Language': 'zh-cn',
# }

# data = 'objectClass=PONYNEW&sk=1b917e89e4664901a5340549b796bb06069615093'

# for i in range(100):
	# response = requests.post('https://newactivity.huazhu.com/v1/wheel/luckyDraw', headers=headers, data=data,verify=False)
	# print(response.json()['value']['data']['point'])
