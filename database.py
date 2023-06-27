import pymongo
from info import DB_NAME, DB_URL

mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["user"]

def set_caption(chat_id, caption):
       dbcol.update_one({"_id": chat_id},{"$set":{"caption": caption}})
	
def get_caption(chat_id): 
        dbcol.update_one({"_id": chat_id},{"$set":{"caption":None}})
    
def set_channel(server_id, target_chat_id):
        dbcol.update_one({"serverid": server_id}, {"$set": {"target_chat_id": target_chat_id}})

def get_channel(server_id, target_chat_id):
        dbcol.find_one({"serverid": server_id}, {"target_chat_id": 1})
        return user.get("target_chat_id", None)

def find_one(id):
	return dbcol.find_one({"_id":id})
