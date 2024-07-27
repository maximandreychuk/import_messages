import json
from random import ranint
from time import sleep
from channels.generic.websocket import WebsocketConsumer


class MsgCounsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for _ in range(1000):
            num = ranint(1, 100)
            self.send(json.dumps({'value': num}))
            sleep(1)
