from pymongo import MongoClient
import os

class Conector():
    def __init__(self):
        # self.addres = os.getenv('ADDRESS')
        self.addres = 'mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/'
        self.db_name = 'IranMalDB'
        self.collection_name = 'tweets'

    def connect(self):
        self.client = MongoClient(self.addres)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def close(self):
        self.client.close()
        self.db = None
        self.collection = None
