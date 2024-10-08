# Reddit Referral Code Poster

This is a simple Python script that posts a referral code to a specified subreddit at regular intervals using the PRAW (Python Reddit API Wrapper) library.

## Features

-   Post a single referral code to a subreddit.
-   Log actions and errors to a specified log file.
-   Configuration is handled through a `.env` file.

## Requirements

-   Python 3.x
-   PRAW
-   python-dotenv

## Obtaining a Reddit API Key

To use the script, you need to create a Reddit API application to obtain your API credentials:

1.  **Go to the Reddit App Preferences**: Navigate to [Reddit App Preferences](https://old.reddit.com/prefs/apps).

2.  **Create a New Application**:

    -   Click on the “Create App” or “Create Another App” button.
    -   Fill in the application details:
        -   **Name**: Choose a name for your application.
        -   **App type**: Select “script.”
        -   **Description**: This can be left blank.
        -   **About url**: This can be left blank.
        -   **Permissions**: This can be left blank.
        -   **Redirect uri**: Set it to `http://localhost:8000` (or any valid URL, but it won't be used for scripts).
    -   Click on the “Create app” button.

3.  **Get Your Credentials**: After creating the app, you will see your `client_id` (just under the webapp title) and `client_secret` (located under the app settings).

## Installation

1.  Clone the repository or download the script.
2.  Install the required packages:

```bash
 pip install -r requirements.txt
```

3.  Create a .env file in the same directory as the script and add your Reddit API credentials and configuration:


    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    USER_AGENT=your_user_agent
    USERNAME=your_username
    PASSWORD=your_password
    SUBREDDIT=your_subreddit
    REFERRAL_CODE=your_referral_code
    LOG_FILE=reddit_bot.log

4.  Run the script:

```bash
python main.py
```

## Logging

The script logs its actions and any errors to a specified log file. You can adjust the log file name in the .env file.

## Setting Up a Cron Job

To run the script automatically at regular intervals using cron, follow these steps:

1.  Open your crontab configuration by running:

```bash
crontab -e
```

2.  Add a new line to specify that you want the script to run every 24 hours. For example, to run the script at midnight every day, add:

```bash
0 0 * * * /usr/bin/python3 /path/to/main.py
```

3.  Save and exit the crontab editor.
