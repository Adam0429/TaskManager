from paho.mqtt import client as mqtt_client

class Producer():
    def __init__(self,id):
        self.broker = 'broker.emqx.io'
        self.port = 1883
        self.client_id = id
        self.client = mqtt_client.Client(self.client_id)
        self.client.connect(self.broker, self.port)

        # def on_connect(client, userdata, flags, rc):
        #     if rc == 0:
        #         print("Connected to MQTT Broker!")
        #     else:
        #         print("Failed to connect, return code %d\n", rc)
        # self.client.on_connect = on_connect

    def publish(self,topic,text):
        result = self.client.publish(topic,text)
        status = result[0]
        if status == 0:
            print(f"Send `{text}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


# producer2 = Producer('python-mqtt-2')
# producer2.publish("TaskManager:send_email",'234')

