import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["blog"]
Post = db["post"]
User = db["user"]


