import random, time, json
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

interaction_types = ['click', 'view', 'purchase']
user_ids = [f"user_{i}" for i in range(1, 101)]
item_ids = [f"item_{i}" for i in range(1, 51)]

while True:
    message = {
        "user_id": random.choice(user_ids),
        "item_id": random.choice(item_ids),
        "interaction_type": random.choice(interaction_types),
        "timestamp": datetime.utcnow().isoformat()
    }
    producer.send("crm-data", message)
    print("Produced:", message)
    time.sleep(1)  # Adjust rate as needed

