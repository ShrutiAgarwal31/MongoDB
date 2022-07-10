import collections
import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)

    print('databases names: ')
    db_names = client.list_database_names()
    print(db_names)

    print('collection names: ')
    collection_names = client['employee']
    print(collection_names.list_collection_names)
