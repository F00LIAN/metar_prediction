# DB Upload Script

This script is designed to hit the [Aviation Weather Center](https://www.aviationweather.gov) to gather weather data for the following airport IDs:

- KSLI (Los Alamitos)
- KLGB (Long Beach)
- KSNA (John Wayne/Orange County)
- KTOA (Torrance)

The data is then uploaded to a database for further analysis and forecasting.

## Key Features

- **Scheduled to run every 15 hours** to ensure the database remains updated with the most recent weather information.
- Automates the data retrieval process from the Aviation Weather Center's METAR reports.

## Installation & Usage

1. Clone the repository:
    ```bash
    git clone git@github.com:F00LIAN/metar_prediction.git
    ```
   
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Schedule the script to run every 15 hours using a cron job or any scheduler of your choice. For example, with cron, you can set it up as follows:
    ```bash
    0 */15 * * * /path/to/python/path/to/script.py
    ```
4. Linux Machines please see the shell command start_metar_script.sh and make a systemctl automated service. Below is the following shell command that loads the environment variables, activates the environment, and runs the script via the systemctl service:
    '''bash 
    # Load environment variables from the .env file in linux path
    export $(grep -v '^#' /home/path/to/working/directory/.env | xargs)

    # Activate the virtual environment
    source /home/path/to/working/directory/venv/bin/activate

    # Run the Python script using the virtual environment's Python
    python /home/path/to/working/directory/metar_db_upload.py'''

5. Create a systemd service file and add the following content that attaches the shell command file for automated use. Automatically updating the database every 15 hours. 
    '''bash
    [Unit]
	Description=METAR Data Fetcher

	[Service]
	Type=simple
	Restart=always
	RestartSec=1
	User=julian
	WorkingDirectory=/home/path/to/working/directory/
	ExecStart=/home/path/to/working/directory/start_metar_script.sh
	EnvironmentFile=/home/path/to/working/directory/.env

	[Install]
	WantedBy=multi-user.target '''

## Database

The script uploads the gathered data into a pre-configured mongodb database. Ensure your database credentials are correctly set up in the environment or configuration file.

## Future Improvements

- Add more airport IDs as needed.
- Integrate data visualizations directly from the database.
- Expand the scheduling options for more flexible runtimes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
