from pymongo import MongoClient
client1 = MongoClient('127.0.0.1',27017)
db1 = client1['Manish']
col1 = db1['amazon']

client = MongoClient('10.56.137.20',27017)
db = client['Manish']
col = db['amazon']

for doc in col1.find({}):
    asin = doc['pc']
    col.insert_one({'pc':asin})
collection.insert_one({"review":kal.text,"date":zal.text,"heading":hal.text})
