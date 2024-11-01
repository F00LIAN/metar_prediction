from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://jasotel1:RhAvV6ROjhjPRTYJ@metar.wogch.mongodb.net/")
    print("MongoDB connection successful.")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
