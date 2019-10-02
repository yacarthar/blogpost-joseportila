import pymongo
from pymongo import ReturnDocument
from datetime import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["zed"]
mycol = mydb["post"]




# time_string = '31/05/2019 17:00'
# time_object = datetime.strptime(time_string, "%d/%m/%Y %H:%M")
# mycol.find_one_and_update(
#         {'time': time_string},
#         # {'$set': {'time': Timestamp(time_object, 0)} },
#         {'$set': {'time': time_object  }},
#         return_document=ReturnDocument.AFTER
#         )

# time_string = '21/06/2016 16:20'
# time_object = datetime.strptime(time_string, "%d/%m/%Y %H:%M")
# mycol.insert({ 'time': time_object })


# a = mycol.find({'post_title': {'$not':{'$regex': 'rank'} } })
# # a = mycol.find({})
# for item in a:
#     time_object = datetime.strptime(item['post_time'], "%d/%m/%Y %H:%M")
#     print(item['post_id'])
#     mycol.find_one_and_update(
#             {'post_id': item['post_id']},
#             {'$set': {'post_time': time_object  }},
#             return_document=ReturnDocument.AFTER
#             )