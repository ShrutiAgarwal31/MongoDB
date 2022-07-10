# from http import client
# from dotenv import load_dotenv, find_dotenv
# import os
# import pprint
# from pymongo import MongoClient

# load_dotenv(find_dotenv())
# password = os.environ.get("MONGO_DB")
# connection_string = "mongodb+srv://techwithshruti:{password}@tutorial.hrhgdde.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(connection_string)
# print('bajaj')


import collections
import pymongo

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
