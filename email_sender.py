import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Email_sender:
    def __init__(self,account,password,smtp_server):
        self.account = account
        self.password = password
        # smtp_server = 'smtp.qq.com'
        self.server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        # server.set_debuglevel(1)  这是输出日志
        self.server.login(account, password)

    def send(self,receivers,subject,text):
        message = MIMEText(text, 'plain', 'utf-8')
        message['From'] = Header(subject, 'utf-8')
        message['To'] = Header("", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        self.server.sendmail(self.account, receivers, message.as_string())
        print('已发送！！！')
        # server.quit()




