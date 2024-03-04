import argparse
from bson.objectid import ObjectId

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from create_db import create_db

uri = f"mongodb://localhost:27017/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.mds

def read_all():
    if db.cats.count_documents({}) == 0:
        print("Database is empty")
    else: 
        [print(cat) for cat in db.cats.find()]

def default():
    clear(1)
    create_db()
    print("Database defaulted!")


def read_by_name():
    name = input("Enter name: ")
    document = db.cats.find_one({"name": name})
    if document is not None:
        return document
    else:
        return "Not found"


def update_age_by_name():
    name = input("Enter name: ")
    document = db.cats.find_one({"name": name})
    if document is not None:
        print('Current age: ', document["age"])
        age = input("Enter new age (integer): ")
        if age.isdigit():
            return db.cats.update_one(document, {"$set": {"age": int(age)}})
        else:
            return "Wrong age"
    else:
        return "Not found"


def update_features():
    name = input("Enter name: ")
    document = db.cats.find_one({"name": name})
    if document is not None:
        features = document["features"]
        print('Current features: ', features)
        new_feature = input("Enter new feature: ")
        features.append(new_feature)
        return db.cats.update_one({"_id": document["_id"]}, {"$set": {"features": features}})
    else:
        return "Not found"


def delete():
    name = input("Enter name: ")
    document = db.cats.find_one({"name": name})
    if document is not None:
        return db.cats.delete_one(document)
    else:
        return "Not found"
    

def clear(silent = 0):
    if silent == 1:
        db.cats.delete_many({})
    else:
        confirm = input("Sure [y/n]?: ").casefold()
        match confirm:
            case "y":    
                return db.cats.delete_many({})
            case "n":
                return "Aborted"
            case _:
                return "Unknown action"
    


if __name__ == "__main__":
    # update_features("65e0d45d163ab0bc774aedba", ["білий", "сірий"])
    if db.cats.find() is None:
        create_db()
    print('Current database:')
    read_all()
    print("Actions: default, read-all, read, update-age, update-features, delete, clear, exit")
    
    while True:   
        action = input("Enter action: ").casefold()
        match action:
            case "read-all":
                read_all()
            case "read":
                print(read_by_name())
            case "update-age":
                print(update_age_by_name())
            case "update-features":
                print(update_features())    
            case "delete":
                print(delete())
            case "clear":
                print(clear(0))
            case "exit":
                print("Bye")
                break
            case "default":
                default()
            case _:
                print("Unknown action")

