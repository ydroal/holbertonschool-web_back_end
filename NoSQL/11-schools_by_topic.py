#!/usr/bin/env python3
"""
Provides a function to list school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    list school having a specific topic

    Args:
    mongo_collection: pymongo collection object
    topics (str): The topics to be searched

    Returns: list of school
    """
    return list(mongo_collection.find({'topics': {'$in': [topic]}}))
