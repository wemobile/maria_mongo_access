from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)

print('---------- database names')
print(client.list_database_names())

# DB access
db = client['myDB']

print('---------- collection names')
for item in db.list_collection_names():
    print(item)
    
# collection access
coll = db['myColl_01']

# print all documents
print('---------- all documents')
for doc in coll.find():
    print(doc)

# document query
print('---------- name query')
for doc in coll.find({"name": "홍길동"}):
    print(doc)
    
print('---------- 2 documents add')
user_profiles = [
    {"name": "임신중", "age": 28},
    {"name": "박찬호", "age": 45}
]
result = coll.insert_many(user_profiles)
# print all documents
print('---------- all documents')
for doc in coll.find():
    print(doc)
    
print('---------- 2 documents add with an additional field')
user_profiles = [
    {"name": "수호자", "age": 25, "MBTI": "ISFJ"},
    {"name": "전략가", "age": 26, "MBTI": "INTJ"}
]
result = coll.insert_many(user_profiles)
# print all documents
print('---------- all documents')
for doc in coll.find():
    print(doc)
    
client.close()