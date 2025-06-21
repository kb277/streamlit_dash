from kafka import KafkaConsumer
import json
from pymongo import MongoClient
from collections import defaultdict

# Connect to Kafka
consumer = KafkaConsumer(
    'crm-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='streaming-consumer'
)

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["interaction_db"]
collection = db["aggregated_data"]

# Aggregation dictionaries
user_interactions = defaultdict(int)
item_counts = defaultdict(int)

print("Kafka consumer started... Listening for messages")

for message in consumer:
    print("📨 Kafka message received")	
    data = message.value
    user_id = data["user_id"]
    item_id = data["item_id"]

    # Update counts
    user_interactions[user_id] += 1
    item_counts[item_id] += 1

    # Upsert user interactions
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"interactions": user_interactions[user_id]}},
        upsert=True
    )

    # Upsert item interactions
    collection.update_one(
        {"item_id": item_id},
        {"$set": {"interactions": item_counts[item_id]}},
        upsert=True
    )

    print(f"Upserted into MongoDB: {data}")

