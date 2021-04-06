from configparser import ConfigParser
from consumer import Consumer
import logging
from logging.handlers import TimedRotatingFileHandler

class LogConsumer(Consumer):
    def __init__(self,id,logger):
        self.topic = 'TaskManager:log'
        self.logger = logger
        super().__init__(id)

    def subscribe(self):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            self.logger.info(msg.payload.decode())
        self.client.on_message = on_message
        self.client.subscribe(self.topic)

    def config(self):
        formatter = logging.Formatter(
            "[%(asctime)s][%(module)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
        handler = TimedRotatingFileHandler(
            "flask.log", when="D", interval=1, backupCount=15,
            encoding="UTF-8", delay=False, utc=True)
        handler.setFormatter(formatter)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def start(self):
        super().start()

    def stop(self):
        super().stop()

if __name__ == '__main__':
    consumer = LogConsumer('123',logger=logging.getLogger(__name__))
    consumer.start()
    while 1:
        pass


