from pymongo import MongoClient


class MongoHelper:

    def __init__(self, server, port, database):
        self.__server = server
        self.__port = port
        self.__database = database
        self.__mongo_client = MongoClient(server, port)

        
    def get_collection(self, name):
        return self.__mongo_client[self.database].getCollection(name)
