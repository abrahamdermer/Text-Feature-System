from abc import ABC,abstractmethod

class IData_loader(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_all_data(self):
        pass