from paho.mqtt import client as mqtt_client
from email_sender import Email_sender
from configparser import ConfigParser

class Consumer():
    def __init__(self,id,topics):
        self.client = mqtt_client.Client(id)
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print(id,"Connected to MQTT Broker!")
            else:
                print(id,"Failed to connect, return code %d\n", rc)
        self.client.on_connect = on_connect
        self.client.connect('test.jmqtt.io', 1883)
        self.subscribe(topics)
        self.config_email()

    def subscribe(self,topics):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            if msg.topic == 'TaskManager:send_email':
                self.email_sender.send(self.receivers,'TaskManager:send_email',msg.payload.decode())
        self.client.on_message = on_message
        for topic in topics:
            self.client.subscribe(topic)

    def config_email(self):
        self.config = ConfigParser()
        self.config.read('default_config.conf')
        self.email_sender = Email_sender(self.config.get('email', 'account'), self.config.get('email', 'password'),self.config.get('email', 'server'))
        self.receivers = eval(self.config.get('email', 'receivers'))
        self.client.subscribe('TaskManager:send_email')

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

if __name__ == '__main__':
    consumer = Consumer('123',['TaskManager:send_email'])
    consumer.start()
    while 1:
        pass
    # consumer.subscribe(['TaskManager:send_email'])


