from pymongo import MongoClient


def get_db_handle(db_name):
    client = MongoClient()
    db_handle = client[db_name]
    return client, db_handle
