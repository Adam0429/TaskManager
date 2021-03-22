from configparser import ConfigParser
from consumer import Consumer
import logging


class LogConsumer(Consumer):
    def __init__(self,id):
        self.topic = 'TaskManager:log'
        super().__init__(id,self.topic)

    def subscribe(self,topics):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            logging.info(msg.payload.decode())
        self.client.on_message = on_message
        self.client.subscribe(self.topic)

    def config(self):
        # 通过下面的方式进行简单配置输出方式与日志级别
        logging.basicConfig(filename='logger.log', level=logging.INFO)

    def start(self):
        super().start()

    def stop(self):
        super().stop()

if __name__ == '__main__':
    consumer = LogConsumer('123')
    consumer.start()
    while 1:
        pass


