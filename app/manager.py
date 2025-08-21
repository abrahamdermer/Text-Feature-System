from dal.functions.data_loader import Data_loader
from processor import Text_proceessor

class Manager():

    def __init__(self):
        self.dal = Data_loader()

    def full_data(self):
        self.data = self.dal.get_all_data()

    def to_df(self):
        self.processor = Text_proceessor(self.data)
        self.processor.to_df()

    def process(self):
        self.processor.process_data()

    def get_df(self):
        return self.processor.get_df()
    
    def to_json(self):
        self.processor.to_json()
    
    def get_json(self):
        return self.processor.get_json()

# maneger = Manager()
# maneger.full_data()
# maneger.to_df()
# # print(maneger.processor.df)
# # maneger.processor.classification()
# # # print(maneger.processor.df)
# # maneger.processor.weapons_detected()
# # print(maneger.processor.df)
# maneger.process()
# # print(maneger.get_df())
# maneger.to_json()
# print(maneger.get_json())