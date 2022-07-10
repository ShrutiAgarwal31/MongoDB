import collections
import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["employees"]
    collection = db['employee_info']

    record = {'name': 'akshat'}
    collection.delete_one(record)
