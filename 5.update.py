import collections
import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["employees"]
    collection = db['employee_info']

    previous = {'name': 'shruti'}
    nextt = {'$set': {'salary': 35000}}
    updated_salary = collection.update_one(previous, nextt)
    # collection.update_many(previous, nextt) ==> update the salary across all shruti's
    print(updated_salary.modified_count)
