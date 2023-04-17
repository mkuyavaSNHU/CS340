from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:55803/AAC' %("aacuser","password"))
        self.database = self.client['AAC']

# Complete this create method to implement the C in CRUD.
    def create(self, data =None):
        if data is not None: 
            insert = self.database.animals.insert_one(data)  # data should be dictionary            
            if insert!=0:
                return True
            else:
                return False    
        else:
            raise Exception("Data parameter is empty. Nothing to save.")

# Create method to implement the R in CRUD. 
    def read(self, criteria=None):
        if criteria is not None: #If the criteria is not empty
            data = self.database.animals.find(criteria,{"_id": False})
        else:
            data = self.database.animals.find({},{"_id": False})
        return data

# Create method to implement the U in CRUD. 
    def update(self, query=None, data=None):
        if data is not None:    
            data_update = self.database.animals.update_one(query, {"$set": data})
            return data_update
        else:
            raise Exception("Data parameter is empty or incorrectly formatted Unable to update.")

# Create method to implement the D in CRUD.
    def delete(self,data=None):
        if data is not None:    
            data_delete = self.database.animals.delete_one(data)
            return data_delete
        else:
            raise Exception("Data parameter is empty or incorrectly formatted. Unable to delete.")
            