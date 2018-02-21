from channels.consumer import SyncConsumer

class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

        self.send({
            "type": "websocket.send",
            "text": "hey I'm socket",
        })