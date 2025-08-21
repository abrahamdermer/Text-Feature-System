from dal.interfacess.dal_interface import IData_loader
from dal.functions.db_connector import Conector

class Data_loader(IData_loader):

    def __init__(self):
        self.connector = Conector()
        self.connector.connect()
        self.collection = self.connector.collection

    def get_all_data(self)->list:
        return list(self.collection.find({}).limit(5))
# .limit(5)