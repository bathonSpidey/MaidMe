from pymongo import MongoClient
import gridfs
from Employee import Employee
import numpy as np

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
        args=collection.find_one(query)
        employee=Employee(**args)
        return employee

    def FindOne(self, collectionName, field, value):
        collection = self.database[collectionName]
        return collection.find_one({field : {"$regex" : value}})

    def FindAll(self, collectionName, field, value):
        collection = self.database[collectionName]
        entries=[]
        for entry in collection.find({field : {"$regex" : value}}):
            entries.append(entry)
        return entries

    def DeserializeImage(self, entry):
        imageEntry=entry["Image"]
        codedImage=self.fileSystem.get(imageEntry["imageID"])
        image=np.frombuffer(codedImage.read(), dtype=np.uint8)
        image=np.reshape(image, imageEntry["shape"])
        return image












