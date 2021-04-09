import smtplib
from smtplib import SMTPServerDisconnected
from email.mime.text import MIMEText
from email.header import Header
from configparser import ConfigParser
from retrying import retry

class Email_sender:
    def __init__(self,account,password,smtp_server):
        self.account = account
        self.password = password
        self.smtp_server = smtp_server
        self.server = smtplib.SMTP(self.smtp_server, 25)  # SMTP协议默认端口是25
        self.server.login(self.account, self.password)

    @retry(stop_max_attempt_number=10, wait_random_min=1000, wait_random_max=1000)
    def send(self,receivers,subject,text):
        message = MIMEText(text, 'plain', 'utf-8')
        message['From'] = Header(subject, 'utf-8')
        message['To'] = Header("", 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
        try:
            self.server.sendmail(self.account, receivers, message.as_string())
        except:#except SMTPServerDisconnected:
            self.server = smtplib.SMTP(self.smtp_server, 25)
            self.server.login(self.account, self.password)
            self.server.sendmail(self.account, receivers, message.as_string())



if __name__ == '__main__':
    config = ConfigParser()
    config.read('default_config.conf')
    email_sender = Email_sender(config.get('email', 'account'), config.get('email', 'password'),
                                     config.get('email', 'server'))
    receivers = eval(config.get('email', 'receivers'))
    email_sender.send(receivers, '123', 'test')
