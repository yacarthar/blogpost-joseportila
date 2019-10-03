import pymongo
from pymongo import ReturnDocument
from datetime import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["zed"]

mycol = mydb["post"]
# mycol = mydb["dmz"]



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


a = mycol.find()
for item in a:
    time_object = datetime.strptime(item['time'], "%d/%m/%Y %H:%M")
    print(item['pid'])
    mycol.find_one_and_update(
            {'pid': item['pid']},
            {'$set': {'time': time_object  }},
            return_document=ReturnDocument.AFTER
            )