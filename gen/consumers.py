from channels.generic.websocket import AsyncWebsocketConsumer
import json
import string, random
from .models import Password
from channels.db import database_sync_to_async


class Consumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = "pass"
        self.room_group_name = f"group_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):

        data  = json.loads(text_data)
        value = int(data.get('value')) 
        number = data.get('number')
        symbol = data.get('symbol')
        savePassToDb = data.get('savePassToDb')

        raw_password = string.ascii_letters
        if(number):
            raw_password += string.digits
        if(symbol):
            raw_password += string.punctuation
        
        password = ''.join(random.choice(raw_password) for _ in range(value))


        if(savePassToDb):
            await database_sync_to_async(Password.objects.create)(password=password)


        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'pass_gen',
                'password':password,
                'savePassToDb':savePassToDb,
            }
        )

    async def pass_gen(self, event):

        await self.send(text_data=json.dumps({
            'password':event['password'],
            'savePassToDb': event['savePassToDb'],
        }))

    async def disconnect(self, closde_code):

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )