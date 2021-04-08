from paho.mqtt import client as mqtt_client
from configparser import ConfigParser
import paho.mqtt.client as mqtt

class Consumer():
    def __init__(self,id):
        self.client = mqtt_client.Client(id)
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print(id,"Connected to MQTT Broker!")
            else:
                print(id,"Failed to connect, return code %d\n", rc)
        self.client.on_connect = on_connect

        config = ConfigParser()
        config.read('default_config.conf')
        server = config.get('mqtt', 'server')
        port = int(config.get('mqtt', 'port'))

        # self.client.username_pw_set(username="admin", password="password")# 必须设置，否则会返回「Connected with result code 4」
        self.client.connect(server, port)
        self.subscribe()
        self.config()

    def config(self):
        pass

    def subscribe(self):
        pass

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()

if __name__ == '__main__':
    consumer = Consumer('123')
    consumer.start()
    while 1:
        pass





