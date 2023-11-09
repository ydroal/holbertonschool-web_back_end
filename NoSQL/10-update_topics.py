#!/usr/bin/env python3
"""
Provides a function to changes all topics of a school document
based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the school name

    Args:
    mongo_collection: pymongo collection object
    name (str): The name of the school to update
    topics (list of str): The list of topics to be set for the school

    Returns: Nothing
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
