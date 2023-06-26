import pymongo
from info import DB_NAME, DB_URL

mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

class Database:

def set_caption(chat_id, caption):
       dbcol.update_one({"_id": chat_id},{"$set":{"caption": caption}})
	
def caption(chat_id): 
        dbcol.update_one({"_id": chat_id},{"$set":{"caption":None}})
    
    async def (self, id, caption):
        await self.col.update_one({'_id': int(id)}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return user.get('caption', None)

    async def set_channel(self, server_id, target_chat_id):
        self.col.update_one({"serverid": server_id}, {"$set": {"target_chat_id": target_chat_id}})

    async def get_channel(self, server_id):
        user = await self.col.find_one({"serverid": server_id}, {"target_chat_id": 1})
        return user.get("target_chat_id", None)

db = Database(DB_URL, DB_NAME)
