import collections
import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["employees"]
    collection = db['employee_info']

    one_doc = collection.find_one({'name': 'shruti'})
    print(one_doc)

    print('\nAll Docs: ')
    all_doc = collection.find()
    for item in all_doc:
        print(item)

    print(collection.find({'name': 'komil'}).count())

    # 1==>inclue that field, 0==>exclude that field
    print('\nNames of employees: ')
    only_names = collection.find({}, {'name': 1, '_id': 0})
    for item in only_names:
        print(item['name'])
