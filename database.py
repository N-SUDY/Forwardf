import motor.motor_asyncio
from info import DB_NAME, DB_URL

class Database:

      async def set_caption(self, id, caption):
        await self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('caption', None)


db = Database(DB_URL, DB_NAME)
