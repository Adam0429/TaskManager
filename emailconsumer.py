from paho.mqtt import client as mqtt_client
from email_sender import Email_sender
from configparser import ConfigParser
from consumer import Consumer

class EmailConsumer(Consumer):
    def __init__(self,id):
        self.topic = 'TaskManager:send_email'
        self.config_email()
        super().__init__(id,self.topic)


    def subscribe(self,topics):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            self.email_sender.send(self.receivers,self.topic,msg.payload.decode())
        self.client.on_message = on_message
        self.client.subscribe(self.topic)

    def config_email(self):
        self.config = ConfigParser()
        self.config.read('default_config.conf')
        self.email_sender = Email_sender(self.config.get('email', 'account'), self.config.get('email', 'password'),self.config.get('email', 'server'))
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
    consumer.subscribe(['TaskManager:send_email'])


