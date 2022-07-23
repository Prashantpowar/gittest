import pymongo



client = pymongo.MongoClient("mongodb+srv://Levi:Naruto@cluster0.titaz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Prashant",
    "email" : "prashantpowar06@gmail.com",
    "surname" : "Powar"
}

db1 = client['mangotest']
coll = db1['test']
coll.insert_one(d)
