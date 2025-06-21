import streamlit as st
from pymongo import MongoClient
import pandas as pd

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["interaction_db"]
collection = db["aggregated_data"]


st.set_page_config(page_title="Interaction Dashboard", layout="wide")
st.title("Real-Time Interaction Dashboard")

# Fetch all documents
docs = list(collection.find({}))

# Safely filter documents
user_docs = [doc for doc in docs if "user_id" in doc and "interactions" in doc]
item_docs = [doc for doc in docs if "item_id" in doc and "interactions" in doc]

# Convert to DataFrames
df_users = pd.DataFrame(user_docs)
df_items = pd.DataFrame(item_docs)

# UI
col1, col2 = st.columns(2)

with col1:
    st.metric("Unique Users", len(df_users))
    if not df_users.empty:
        st.bar_chart(df_users.set_index("user_id")["interactions"])
    else:
        st.info("No user interaction data found.")

with col2:
    st.metric("Unique Items", len(df_items))
    if not df_items.empty:
        st.bar_chart(df_items.set_index("item_id")["interactions"])
    else:
        st.info("No item interaction data found.")

