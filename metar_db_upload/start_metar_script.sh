#!/bin/bash

# Load environment variables from the .env file
export $(grep -v '^#' /home/julian/Desktop/metar_db_upload/.env | xargs)

# Activate the virtual environment
source /home/julian/Desktop/metar_db_upload/venv/bin/activate

# Run the Python script using the virtual environment's Python
python /home/julian/Desktop/metar_db_upload/metar_db_upload.py