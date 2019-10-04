import pymongo
from pymongo import ReturnDocument
from datetime import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["blog"]

User = mydb["user"]
Post = mydb["post"]
Dmz = mydb["dmz"]


# item = {}
# pid = '166189'
# post = Post.find_one({'pid': pid})
# for k, v in post.items():
#     if k == '_id':
#         continue
#     else:
#         item[k] = v
# Dmz.insert_one(item)


pid = '166189'
Dmz.find_one_and_update(
        {'pid': pid},
        {'$set': {'content': 'mot con vit xoe ra 2 cai canh'  }},
        return_document=ReturnDocument.AFTER
        )

# check update one
# time_string = '31/05/2019 17:00'
# time_object = datetime.strptime(time_string, "%d/%m/%Y %H:%M")
# mycol.find_one_and_update(
#         {'time': time_string},
#         # {'$set': {'time': Timestamp(time_object, 0)} },
#         {'$set': {'time': time_object  }},
#         return_document=ReturnDocument.AFTER
#         )

# check ISODate
# time_string = '21/06/2016 16:20'
# time_object = datetime.strptime(time_string, "%d/%m/%Y %H:%M")
# mycol.insert({ 'time': time_object })
# print('ok')


# a = mycol.find()
# for item in a:
#     time_object = datetime.strptime(item['time'], "%d/%m/%Y %H:%M")
#     print(item['pid'])
#     mycol.find_one_and_update(
#             {'pid': item['pid']},
#             {'$set': {'time': time_object  }},
#             return_document=ReturnDocument.AFTER
#             )