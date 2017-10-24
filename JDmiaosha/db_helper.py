# -*- coding: utf-8 -*-
from pymongo import MongoClient
from .settings import HOST,PORT


class DBHelp:
    def __init__(self,collection_name):
        self.client = MongoClient(HOST, 27017)
        self.db = self.client["JD"]
        self.collection = self.db[collection_name]

    def insert_many(self, data):
        self.collection.insert_many(data)

    def insert_one(self,data):
        self.collection.insert_one(data)

    def find_one(self, key=None):
        return self.collection.find_one(key)

    def find_many(self,key=None):
        return self.collection.find(key)

    def remove(self):
        self.collection.remove()
