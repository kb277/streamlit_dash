# Real-Time User Interaction Dashboard

A real-time data pipeline project that demonstrates message ingestion using **Kafka**, storage and processing using **MongoDB**, and real-time visualization via **Streamlit**. The pipeline simulates user interactions, aggregates data, and visualizes key metrics on a dashboard.

---

## ✨ Features

* Kafka producer simulates user-item interactions
* Kafka consumer processes and stores data into MongoDB
* MongoDB stores both raw and aggregated interaction data
* Streamlit dashboard visualizes:

  * Total interactions
  * Unique users and items
  * Top users/items by interaction count
  * Time series interaction trend (optional)

---

## 🧬 Tech Stack

* **Kafka** (Producer & Consumer)
* **MongoDB** (Database)
* **Python** (Scripting)
* **Streamlit** (Dashboard UI)
* **pymongo**, **kafka-python**, **pandas** (Libraries)

---

## 📚 Project Structure

```
.
├── data_producer.py         # Kafka producer to simulate user interactions
├── consumer.py              # Kafka consumer to ingest and upsert to MongoDB
├── verify_mongo.py         # Utility to verify MongoDB data
├── streamlit_dashboard.py  # Streamlit dashboard for visualization
```

---

## ⚙️ Setup Instructions

### 1. Prerequisites

* Kafka installed and running on localhost (default port: 9092)
* MongoDB installed and running (default URI: mongodb://localhost:27017/)
* Python 3.7+

### 2. Install dependencies

```bash
pip install kafka-python pymongo streamlit pandas plotly
```

### 3. Create Kafka topic

```bash
kafka-topics --create --topic crm-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 4. Run Kafka Producer

```bash
python3 data_producer.py
```

### 5. Run Kafka Consumer

```bash
python3 consumer.py
```

### 6. Verify MongoDB data (optional)

```bash
python3 verify_mongo.py
```

### 7. Run Streamlit Dashboard

```bash
streamlit run streamlit_dashboard.py
```

---

## 📈 Dashboard Metrics

* **Total Interactions**: Count of all interaction records
* **Unique Users**: Number of distinct `user_id`s
* **Unique Items**: Number of distinct `item_id`s
* **Top 10 Users**: Bar chart of top interacting users
* **Top 10 Items**: Bar chart of top interacted items
* **Time Series** *(optional)*: Line chart showing interaction trend

---

## 🎓 Learning Objectives

* Implement a streaming data pipeline
* Understand producer/consumer mechanics in Kafka
* Interact with MongoDB using PyMongo
* Build real-time dashboards with Streamlit

---

## 📊 Example Output

![Dashboard Screenshot](screenshots/streamlit_dashboard.png)

---

## 🚀 Future Enhancements

* Dockerize the entire pipeline
* Add authentication to dashboard
* Integrate with cloud MongoDB (e.g., Atlas)
* Persist consumer offsets for exactly-once s
