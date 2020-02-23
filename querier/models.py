from django.db import models
import pymongo
from querier import method, env

client = pymongo.MongoClient(env.mongoPath)
db = client[env.mongoName]


def findHouseDatas(request):
    return db.coll.find(
        {'name': method.splitPlus(request, 'name'), 'identity': method.default(request, 'identity'), 'city': method.default(request, 'city'),
         'houseCondition': method.default(request, 'houseCondition'), 'houseType': method.default(request, 'houseType'),
         'sex': method.default(request, 'sex'), 'phone': method.splitPlus(request, 'phone')}, {'_id': 0})
