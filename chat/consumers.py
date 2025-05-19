from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name='public_chat'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        from .models import Message_Chat

        if not self.scope['user'].is_authenticated:
            await self.send(text_data=json.dumps({
                'error': 'فقط کاربران لاگین‌کرده می‌توانند پیام ارسال کنند.'
            }))
            return

        data = json.loads(text_data)
        message = data['message']
        user = self.scope['user']

        await sync_to_async(Message_Chat.objects.create)(
            sender=user,
            text=message
        )

        await self.channel_layer.group_send(self.room_group_name, {
            'type': 'chat_message',
            'message': message,
            'user': user.username
        })


    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'user': event['user']
        }))