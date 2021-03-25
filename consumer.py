from paho.mqtt import client as mqtt_client
from configparser import ConfigParser

class Consumer():
    def __init__(self,id,topic):
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

        self.client.connect(server, port)
        self.subscribe(topic)
        self.config()
        # self.config_email()

    def config(self):
        pass

    def subscribe(self,topic):
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


