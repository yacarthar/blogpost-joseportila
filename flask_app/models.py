import pymongo
from config import MONGO_URI, MONGO_DATABASE, MONGO_COLLECTION

myclient = pymongo.MongoClient(MONGO_URI)
Post = myclient[MONGO_DATABASE][MONGO_COLLECTION]
