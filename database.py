import motor.motor_asyncio
from info import DB_NAME, DB_URL

class Database:

    async def set_caption(self, id, caption):
        await self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('caption', None)

    async def set_channel(self, server_id, channel_id):
        self.col.update_one({"serverid": server_id}, {"$set": {"channelid": channel_id}})

    async def get_channel(self, server_id):
        user = await self.col.find_one({"serverid": server_id}, {"channelid": 1})
        return user.get["channelid"]

db = Database(DB_URL, DB_NAME)
