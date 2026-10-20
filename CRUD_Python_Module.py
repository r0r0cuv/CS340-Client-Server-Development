# CRUD Python Module

from pymongo import MongoClient


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password):
        """Initialize the MongoDB connection using supplied credentials."""

        # Connection variables
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        # Initialize MongoDB connection
        self.client = MongoClient(
            HOST,
            PORT,
            username=username,
            password=password,
            authSource='admin'
        )

        # Access the AAC database and animals collection
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method - C in CRUD
    def create(self, data):
        """Insert a document into the animals collection."""

        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print("Create error:", e)
                return False
        else:
            return False

    # Read method - R in CRUD
    def read(self, query):
        """Query documents from the animals collection."""

        if query is not None and isinstance(query, dict):
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as e:
                print("Read error:", e)
                return []
        else:
            return []

    # Update method - U in CRUD
    def update(self, query, new_data):
        """Update documents matching the supplied query."""

        if (
            query is not None
            and isinstance(query, dict)
            and new_data is not None
            and isinstance(new_data, dict)
        ):
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_data}
                )
                return result.modified_count
            except Exception as e:
                print("Update error:", e)
                return 0

        return 0

    # Delete method - D in CRUD
    def delete(self, query):
        """Delete documents matching the supplied query."""

        if query is not None and isinstance(query, dict):
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete error:", e)
                return 0

        return 0