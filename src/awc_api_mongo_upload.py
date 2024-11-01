from pymongo import MongoClient
import requests
import json
from datetime import datetime

# MongoDB Atlas connection setup
try:
    # Full connection URI for a replica set
    client = MongoClient(
        "mongodb://jasotel1:RhAvV6ROjhjPRTYJ@metar-shard-00-00.wogch.mongodb.net:27017,"
        "metar-shard-00-01.wogch.mongodb.net:27017,"
        "metar-shard-00-02.wogch.mongodb.net:27017/"
        "?ssl=true&replicaSet=atlas-11hv04-shard-0&authSource=admin&retryWrites=true&w=majority"
    )
    db = client['aviation_weather_center']  # Database name
    collection = db['metar_reports']  # Collection name
    print("MongoDB connection successful.")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

# METAR API endpoint
url = "https://aviationweather.gov/api/data/metar"
airport_ids = ['KSLI', 'KLGB', 'KSNA', 'KTOA']
metar_hours_back = 15
format_response = 'json'

# Function to get METAR data for specified airports
def get_metar_data():
    for airport in airport_ids:
        try:
            # Make request to METAR API for each airport
            response = requests.get(f"{url}?ids={airport}&format={format_response}&hours={metar_hours_back}")
            
            # Check if the response is successful
            if response.status_code == 200:
                try:
                    metar_data = response.json()

                    # Check if the response is a list (new format)
                    if isinstance(metar_data, list):
                        for report in metar_data:
                            # Use 'metar_id' as the unique identifier
                            report_id = report.get('metar_id')

                            # Check if report already exists in MongoDB
                            try:
                                if report_id and collection.count_documents({'metar_id': report_id}) == 0:
                                    # Add a timestamp for data tracking and insert into MongoDB
                                    report['timestamp'] = datetime.utcnow()
                                    collection.insert_one(report)
                                    print(f"Inserted METAR report for {airport} with metar_id: {report_id}")
                                else:
                                    print(f"Duplicate found for {airport} with metar_id: {report_id} - Skipping")
                            except Exception as e:
                                print(f"MongoDB operation failed: {e}")
                    else:
                        print(f"Unexpected response format for {airport}: {metar_data}")
                except json.JSONDecodeError:
                    print(f"Failed to decode JSON response for {airport}. Response: {response.text}")
            else:
                print(f"Failed to fetch data for {airport}. HTTP Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {airport}: {e}")

# The entry point of the script
if __name__ == "__main__":
    get_metar_data()
