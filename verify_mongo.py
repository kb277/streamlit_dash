from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access DB and collection
db = client["interaction_db"]
collection = db["aggregated_data"]

# Fetch and print documents
print("Verifying MongoDB contents:")
for doc in collection.find().limit(10):
    print(doc)

