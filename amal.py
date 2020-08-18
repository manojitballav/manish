from pymongo import MongoClient


client = MongoClient('10.56.133.247',27017)
db = client['Manish']
col = db['RedmiNote9']
col1 = db['B08695YMYC']
col2 = db['B08695YRKV']
col3 = db['B086984LHS']
col4 = db['B086977TR6']
col5 = db['B08696ZMPF']
col6 = db['B086KCC68B']

# db.Redmi Note 9 Pro.renameCollection('RedmiNote9')
# col1.update_many({},{'$set': {"RAM": '4 GB',"ROM": '64 GB', "color": 'Aqua Green'}},upsert = True)
# col2.update_many({},{'$set': {"RAM": '4 GB',"ROM": '128 GB', "color": 'Pebble Grey'}},upsert = True)
# col3.update_many({},{'$set': {"RAM": '4 GB',"ROM": '64 GB', "color": 'Scarlet Red'}},upsert = True)
# col4.update_many({},{'$set': {"RAM": '4 GB',"ROM": '64 GB', "color": 'Pebble Grey'}},upsert = True)
# col5.update_many({},{'$set': {"RAM": '4 GB',"ROM": '128 GB', "color": 'Aqua Green'}},upsert = True)
col6.update_many({},{'$set': {"RAM": '4 GB',"ROM": '64 GB', "color": 'Violet'}},upsert = True)

# for doc in col5.find({}):
#     heading = doc['heading']
#     # print(heading)
#     review = doc['review']
#     date = doc['date']
#     rating = doc['rating']
#     RAM = doc['RAM']
#     ROM = doc['ROM']
#     color = doc['color']
#     col.insert({"review":review,"date":date,"heading":heading,"rating":rating,"ROM":ROM,"RAM":RAM,"color":color})

#     # col.update_many({},{'$set':{"review":review,"date":date,"heading":heading,"rating":rating,"ROM":ROM,"RAM":RAM,"color":color}},upsert=True)