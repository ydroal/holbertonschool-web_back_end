#!/usr/bin/env python3
"""
Provides a function to list all documents within a MongoDB collection
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    return list(mongo_collection.find())
