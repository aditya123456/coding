from abc import ABC, abstractmethod


class FrontEnd:

    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display Data", data)


class BackEnd:

    def get_data_from_database(self):
        return "Data from the database"






class FronEndDI:

    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display Data", data)


class DataSourceDI(ABC):

    @abstractmethod
    def get_data(self):
        pass
class API(DataSourceDI):

    def get_data(self):
        return "Data from the API"