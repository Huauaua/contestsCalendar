# Contests Calendar

## Project Introduction
`Contests Calendar` is a Python tool designed to fetch upcoming programming contest information from Codeforces and NowCoder. It converts the contest start times to Beijing time and saves the contest details into a JSON file on the desktop. This tool is useful for competitive programmers who want to track upcoming contests in a structured format.

## Features
1. **Fetch Contest Information**:
   - Extracts contest details from Codeforces and NowCoder.
   - Filters contests that are scheduled to start on or after the current date.
2. **Time Conversion**:
   - Converts contest start times from UTC to Beijing time.
3. **Data Persistence**:
   - Saves contest information to a `contests.json` file on the desktop.
   - If the file already exists, it merges new data with existing entries and removes duplicates.

## Usage
### Environment Dependencies
The following libraries are required to run this tool. Please ensure they are installed:

- **Python 3.8 or higher**: Required to run the script.
- **`requests` library**: Used for making HTTP requests to fetch contest information.
- **`colorama` library**: Used for colored terminal output.
- **`json` library**: Used for handling JSON data and saving contest information to a file.
- **`os` library**: Used for file path operations.
- **`datetime`, `timezone`, and `timedelta`**: Used for handling time and time zone conversions.

Install dependencies:
```bash
pip install requests colorama
```
### Configuration
1. **Replace API URLs**:
   - In the `get_codeforces_contests()` function, replace the `url` with the actual Codeforces contest API URL.
   - In the `get_nowcoder_contests()` function, replace the `url` with the actual NowCoder contest API URL.

2. **(Optional) Modify Save Path**:
   - By default, contest information is saved to `contests.json` on the desktop. To change the save path, modify the `desktop_path` in the `save_to_json()` function.
### Notes
1. **API Rate Limits**:
   - Ensure that the API URLs are valid and comply with the terms of service of the respective websites.
   - If the API has rate limits, adjust the request intervals in the script accordingly.

2. **Time Synchronization**:
   - The script converts contest times from UTC to Beijing time. Ensure that your system clock is synchronized with network time.

3. **Automating Updates**:
   - If you need to update contest information frequently, consider setting up a scheduled task (e.g., using `cron` on Linux/macOS or Task Scheduler on Windows).
### Running the Script
Run the script:
```bash
python contestsCalendar.py
```
After running, the script will fetch contest information and save it to `contests.json` on the desktop. If the file already exists, it will merge new data with existing entries and remove duplicates.
### Output File Format
The saved `contests.json` file is a JSON-formatted list, with each contest containing the following fields:
```json
[
    {
        "id": "Contest ID",
        "name": "Contest Name",
        "startTime": "Contest start time (Beijing time, formatted as YYYY-MM-DD HH:MM:SS)",
        "type": "Contest type (e.g., Codeforces or NowCoder)",
        "phase": "Contest status (e.g., BEFORE)",
        "durationSeconds": "Contest duration (formatted as HH:MM:SS)"
    }
]
```
