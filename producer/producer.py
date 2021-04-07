from paho.mqtt import client as mqtt_client
from configparser import ConfigParser
import paho.mqtt.client as mqtt
import time

class Producer():
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

        # self.client.username_pw_set(username="admin", password="password")
        self.client.connect(server, port)

    def publish(self,topic,text):
        # import paho.mqtt.publish as publish
        #
        # publish.single(topic, text, hostname='127.0.0.1', port=61613,
        #                auth={'username': "admin", 'password': "password"})


        result = self.client.publish(topic,text)
        status = result[0]
        if status == 0:
            print(f"Send `{text}` to topic `{topic}` success")
        else:
            print(f"Failed to send `{text}` to topic `{topic}`")

if __name__ == '__main__':
    producer2 = Producer('python-mqtt-2')
    for i in range(10011):
        producer2.publish('TaskManager:send_email',str(i))
        import time
        time.sleep(1)

