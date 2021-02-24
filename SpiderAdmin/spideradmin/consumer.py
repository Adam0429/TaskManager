from paho.mqtt import client as mqtt_client
from email_sender import Email_sender

class Consumer():
    def __init__(self,id):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        self.broker = 'broker.emqx.io'
        self.port = 1883
        self.client_id = id
        self.client = mqtt_client.Client(self.client_id)
        # self.client.on_connect = on_connect
        self.client.connect(self.broker, self.port)


    def subscribe(self,topics):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            email_sender = Email_sender('', '')
            email_sender.send(receivers=['872490934@qq.com'],subject='TaskManager',text=msg.payload.decode())

        for topic in topics:
            self.client.subscribe(topic)
        self.client.on_message = on_message
        self.client.loop_forever()


consumer = Consumer('server')
consumer.subscribe(['TaskManager:send_email'])
