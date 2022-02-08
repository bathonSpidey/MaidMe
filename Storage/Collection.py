from pymongo import MongoClient
import gridfs

class Collection:
    def __init__(self, connectionUrl, database):
        self.connectionUrl=connectionUrl
        self.client=MongoClient(self.connectionUrl)
        self.database=self.client[database]
        self.fileSystem=gridfs.GridFS(self.database)


    def GetCollection(self, name):
        return self.database[name]

    def Add(self,collectionName,entry):
        collection=self.database[collectionName]
        collection.insert_one(entry)

    def FindOneBasedOneFirstName(self,collectionName, entryName ):
        collection = self.database[collectionName]
        query={"FirstName": entryName}
        return collection.find_one(query)

    def FindOne(self, collectionName, field, value):
        collection = self.database[collectionName]
        return collection.find_one({field : {"$regex" : value}})

    def FindAll(self, collectionName, field, value):
        collection = self.database[collectionName]
        entries=[]
        for entry in collection.find({field : {"$regex" : value}}):
            entries.append(entry)
        return entries









