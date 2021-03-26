import smtplib
from email.mime.text import MIMEText
from email.header import Header
from configparser import ConfigParser

class Email_sender:
    def __init__(self,account,password,smtp_server):
        self.account = account
        self.password = password
        # smtp_server = 'smtp.qq.com'
        self.server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        # server.set_debuglevel(1)  这是输出日志
        self.server.login(account, password)

    def send(self,receivers,subject,text):
        try:
            message = MIMEText(text, 'plain', 'utf-8')
            message['From'] = Header(subject, 'utf-8')
            message['To'] = Header("", 'utf-8')
            message['Subject'] = Header(subject, 'utf-8')
            self.server.sendmail(self.account, receivers, message.as_string())
            return 1
        except:
            return 0
        # server.quit()


if __name__ == '__main__':
    config = ConfigParser()
    config.read('default_config.conf')
    email_sender = Email_sender(config.get('email', 'account'), config.get('email', 'password'),
                                     config.get('email', 'server'))
    receivers = eval(config.get('email', 'receivers'))
    email_sender.send(receivers, '123', 'test')
