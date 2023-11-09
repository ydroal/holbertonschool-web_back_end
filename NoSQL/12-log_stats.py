#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    count_documents = collection.count_documents({})
    count_get_method = collection.count_documents({"method": "GET"})
    count_post_method = collection.count_documents({"method": "POST"})
    count_put_method = collection.count_documents({"method": "PUT"})
    count_patch_method = collection.count_documents({"method": "PATCH"})
    count_delete_method = collection.count_documents({"method": "DELETE"})
    count_get_method_and_status = collection.count_documents({
        "method": "GET", "path": "/status"})

    print('{} logs'.format(count_documents))
    print('Methods:')
    print("\tmethod GET: {}".format(count_get_method))
    print("\tmethod POST: {}".format(count_post_method))
    print("\tmethod PUT: {}".format(count_put_method))
    print("\tmethod PATCH: {}".format(count_patch_method))
    print("\tmethod DELETE: {}".format(count_delete_method))
    print('{} status check'.format(count_get_method_and_status))
