from pymongo import MongoClient
from bson.objectid import ObjectId

class CRUD:
    def __init__(self, username, password):
        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@localhost:27017/?authSource=admin"
            )
            self.database = self.client["aac"]
            self.collection = self.database["animals"]
        except Exception as e:
            print("Connection Error:", e)

    # CREATE
    def create(self, data):
        try:
            result = self.collection.insert_one(data)
            return True
        except Exception:
            return False

    # READ
    def read(self, query):
        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except Exception:
            return []

    # UPDATE
    def update(self, query, new_values):
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception:
            return 0

    # DELETE
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception:
            return 0