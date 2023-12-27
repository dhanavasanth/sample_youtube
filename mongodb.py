from pymongo import MongoClient

client = MongoClient("mongodb+srv://danavasanth:rootpassword@cluster0.fwkjhzj.mongodb.net/?retryWrites=true&w=majority")

db = client.Youtube_data

collection = db.channel_data

def connect_mongo(response):
    db.collection.insert_one(response)

    return "successfully inserted"