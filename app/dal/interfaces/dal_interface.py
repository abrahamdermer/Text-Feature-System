from abc import ABC,abstractmethod

class IData_loader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all_data(self):
        pass

    @abstractmethod
    def insert_new_soldier(self,id,first_name,last_name,phone_number,rank):
        pass

    @abstractmethod
    def update_by_id(self,id,fild:dict):
        pass

    @abstractmethod
    def delete_by_id(self,id):
        pass