import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Email_sender:
    def __init__(self,account,password):
        self.account = account
        self.password = password
        smtp_server = 'smtp.qq.com'
        self.server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        # server.set_debuglevel(1)  这是输出日志
        self.server.login(account, password)

    def send(self,receivers,subject,text):
        message = MIMEText(text, 'plain', 'utf-8')
        message['From'] = Header(subject, 'utf-8')  # 发送者
        message['To'] = Header("", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        self.server.sendmail(self.account, receivers, message.as_string())
        # server.quit()


import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883, 600) # 600为keepalive的时间间隔
client.subscribe('fifa', qos=0)
client.loop_forever() # 保持连接