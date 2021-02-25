from paho.mqtt import client as mqtt_client
from email_sender import Email_sender
from configparser import ConfigParser

class Consumer():
    def __init__(self,id):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print(id,"Connected to MQTT Broker!")
            else:
                print(id,"Failed to connect, return code %d\n", rc)
        self.broker = 'test.jmqtt.io'
        self.port = 1883
        self.client_id = id
        self.client = mqtt_client.Client(self.client_id)
        self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)
        self.config_email()

    def config_email(self):
        self.config = ConfigParser()
        self.config.read('/Users/wangfeihong/Desktop/config.conf')
        self.email_sender = Email_sender(self.config.get('email', 'account'), self.config.get('email', 'password'))
        self.receivers = eval(self.config.get('email', 'receivers'))

    def subscribe(self,topics):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            # self.email_sender.send(receivers=self.receivers,subject='TaskManager',text=msg.payload.decode())
        for topic in topics:
            self.client.subscribe(topic)
        self.client.on_message = on_message
        self.client.loop_forever()

if __name__ == '__main__':
    consumer = Consumer('server')
    consumer.subscribe(['TaskManager:send_email'])
