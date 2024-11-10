from pymongo import MongoClient
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

# MongoDB Atlas connection setup
try:
    CONN_1 = os.getenv("CONN_1")
    CONN_2 = os.getenv("CONN_2")
    CONN_3 = os.getenv("CONN_3")
    CONN_4 = os.getenv("CONN_4")

    connection_uri = f"{CONN_1}{CONN_2}{CONN_3}{CONN_4}"

    client = MongoClient(connection_uri)
    db = client['aviation_weather_center']
    collection = db['metar_reports']

    print("MongoDB connection successful")

except Exception as e:
    error_message = f"Failed to connect to MongoDB: {e}"
    print(error_message)
    exit()  # Exit if the database connection fails

# Function to get METAR data for specified airports
def get_metar_data():
    url = "https://aviationweather.gov/api/data/metar"
    airport_ids = ['KSLI', 'KLGB', 'KSNA', 'KTOA']
    metar_hours_back = 15
    format_response = 'json'

    for airport in airport_ids:
        try:
            response = requests.get(f"{url}?ids={airport}&format={format_response}&hours={metar_hours_back}")
            if response.status_code == 200:
                try:
                    metar_data = response.json()
                    if isinstance(metar_data, list):
                        for report in metar_data:
                            report_id = report.get('metar_id')
                            try:
                                if report_id and collection.count_documents({'metar_id': report_id}) == 0:
                                    report['timestamp'] = datetime.utcnow()
                                    collection.insert_one(report)
                                    success_message = f"Inserted METAR report for {airport} with metar_id: {report_id}"
                                    print(success_message)
                                else:
                                    print(f"Duplicate found for {airport} with metar_id: {report_id} - Skipping")
                            except Exception as e:
                                error_message = f"MongoDB operation failed: {e}"
                                print(error_message)
                    else:
                        warning_message = f"Unexpected response format for {airport}: {metar_data}"
                        print(warning_message)
                except json.JSONDecodeError:
                    error_message = f"Failed to decode JSON response for {airport}. Response: {response.text}"
                    print(error_message)
            else:
                error_message = f"Failed to fetch data for {airport}. HTTP Status: {response.status_code}"
                print(error_message)
        except requests.exceptions.RequestException as e:
            error_message = f"Error fetching data for {airport}: {e}"
            print(error_message)

# The entry point of the script
if __name__ == "__main__":
    while True:
        get_metar_data()
        print("Waiting for the next update in 15 hours...")
        time.sleep(15 * 60 * 60)  # Sleep for 15 hours
