from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

class Conector():
    def __init__(self):
        self.addres = os.getenv('ADDRESS')
        self.db_name = os.getenv('DB_NAME')
        self.collection_name = os.getenv('COLLETION_NAME')

    def connect(self):
        self.client = MongoClient(self.addres)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def close(self):
        self.client.close()
        self.db = None
        self.collection = None