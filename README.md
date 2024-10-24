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
    0 */15 * * * /path/to/python /path/to/script.py
    ```

## Database

The script uploads the gathered data into a pre-configured database. Ensure your database credentials are correctly set up in the environment or configuration file.

## Future Improvements

- Add more airport IDs as needed.
- Integrate data visualizations directly from the database.
- Expand the scheduling options for more flexible runtimes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
