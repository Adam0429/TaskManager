from templates.email_sender import Email_sender
from configparser import ConfigParser
if __name__ == '__main__':
    from consumer import Consumer
else:
    from consumer.consumer import Consumer

class EmailConsumer(Consumer):
    def __init__(self,id):
        self.topic = 'TaskManager:send_email'
        super().__init__(id)

    def subscribe(self):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            try:
                self.email_sender.send(self.receivers,self.topic,msg.payload.decode())
                self.publish('TaskManager:log', '邮件发送成功！')
            except:
                self.publish('TaskManager:log', '邮件发送失败！')
        self.client.on_message = on_message
        self.client.subscribe(self.topic)

    # 这里为了记录邮件发送的日志，所以添加了publish功能
    def publish(self, topic, text):
        result = self.client.publish(topic, text)
        status = result[0]
        if status == 0:
            print(f"Send `{text}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def config(self):
        self.config = ConfigParser()
        self.config.read('default_config.conf')
        try:
            self.email_sender = Email_sender(self.config.get('email', 'account'), self.config.get('email', 'password'),self.config.get('email', 'server'))
        except:
            self.publish('TaskManager:log','邮件配置错误！')
        self.receivers = eval(self.config.get('email', 'receivers'))

    def start(self):
        super().start()

    def stop(self):
        super().stop()

if __name__ == '__main__':
    consumer = EmailConsumer('123')
    consumer.start()
    while 1:
        pass


