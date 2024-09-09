import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print('connected>>>>>')
        # print(self.scope["url_route"]["kwargs"]["chat_box_name"])
        # print(self.scope)
        # Called when the WebSocket handshake is successful
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = "chat_%s" % self.chat_box_name
        # # self.group_name = "message_1100"
        
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # print('disconnected')
        # Called when the WebSocket connection is closed
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        

    async def receive(self, text_data):
        print('receive')
        # Called when a message is received from the WebSocket
        text_data_json = json.loads(text_data)
        # print(text_data_json,'weebbbssss')
        chat_id = text_data_json['chat_id']
        # message_id = text_data_json['message_id']
        # user_id = text_data_json['user_id']
        # text = text_data_json['text']
        # owner = text_data_json['owner']
        # image = text_data_json['image']
        # username = text_data_json['username']
        # msg_type = text_data_json['msg_type']
        # file = text_data_json['file']

        # Process the message and prepare the response
        chanell = self.channel_layer
        # chanell['client'][0]='3.89.144.86'
        # chanell['client'][1]='80'
        print(self.channel_layer,self.scope,'befor<<<<<<<')
        await self.channel_layer.group_send(
            self.group_name,
            {
                "client":['3.89.144.86','80'],
                "type": "chatbox_message",
                "chat_id": chat_id,
                # "message_id": message_id,
                # "user_id": user_id,
                # "text": text,
                # "owner": owner,
                # "image":image,
                # "username":username,
                # "msg_type":msg_type,
                # "file":file
            },
        )
        print('after>>>>>> ',self.channel_layer,self.scope)

        # Send the response back to the connected client
        # print(response_message)
        # await self.send(text_data=json.dumps({'message': response_message}))
        # print(self)
    async def chatbox_message(self, event):
        print('send>>>')
        chat_id = event["chat_id"]
        # message_id = event["message_id"]
        # user_id = event["user_id"]
        # text = event["text"]
        # owner = event["owner"]
        # image = event["image"]
        # username = event["username"]
        # msg_type = event["msg_type"]
        # file = event["file"]

        message_data = {
            "chat_id": chat_id,
            # "message_id": message_id,
            # "user_id": user_id,
            # "text": text,
            # "owner": owner,
            # "image": image,
            # "username": username,
            # "msg_type": msg_type,
            # "file": file
        }
        await self.send(text_data=json.dumps(message_data))
        