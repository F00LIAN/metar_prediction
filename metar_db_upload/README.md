# DB Upload Script

This script fetches weather data from the [Aviation Weather Center](https://www.aviationweather.gov) for the following airport IDs:

- **KSLI**: Los Alamitos
- **KLGB**: Long Beach
- **KSNA**: John Wayne/Orange County
- **KTOA**: Torrance

The data is then uploaded to a database for further analysis and forecasting.

## Key Features

- **Scheduled to run every 15 hours**: Ensures the database stays updated with the latest weather information.
- **Automates METAR data retrieval**: Automatically fetches data from the Aviation Weather Center’s METAR reports.

## Installation & Usage

1. **Clone the repository**:
    ```bash
    git clone git@github.com:F00LIAN/metar_prediction.git
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Schedule the script to run every 15 hours** using a cron job or any scheduler of your choice. For example, with cron, you can set it up as follows:
    ```bash
    0 */15 * * * /path/to/python /path/to/script.py
    ```

4. **For Linux users**, please see the `start_metar_script.sh` file and create a systemd service for automated script execution. Below is the shell command to load environment variables, activate the virtual environment, and run the script via systemd:
    ```bash
    # Load environment variables from the .env file
    export $(grep -v '^#' /home/path/to/working/directory/.env | xargs)

    # Activate the virtual environment
    source /home/path/to/working/directory/venv/bin/activate

    # Run the Python script using the virtual environment's Python
    python /home/path/to/working/directory/metar_db_upload.py
    ```

5. **Create a systemd service** to automatically update the database every 15 hours. Add the following content to a new service file:
    ```bash
    [Unit]
    Description=METAR Data Fetcher

    [Service]
    Type=simple
    Restart=always
    RestartSec=1
    User=your_username
    WorkingDirectory=/home/path/to/working/directory/
    ExecStart=/home/path/to/working/directory/start_metar_script.sh
    EnvironmentFile=/home/path/to/working/directory/.env

    [Install]
    WantedBy=multi-user.target
    ```

## Database

The script uploads the gathered data to a pre-configured MongoDB database. Ensure your database credentials are correctly set up in the environment or configuration file.

## Future Improvements

- Add support for additional airport IDs.
- Integrate data visualizations directly from the database.
- Expand scheduling options for more flexible runtimes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
