# Reddit Referral Code Poster

![image](image.jpg)

This Python script automates the process of obtaining a Reddit API refresh token and posts a referral code to a specified subreddit at regular intervals using the PRAW (Python Reddit API Wrapper) library.

## Features

- Automated OAuth2 authentication flow for obtaining a refresh token
- Post a single referral code to a subreddit
- Log actions and errors to a specified log file
- Configuration handled through a `.env` file
- Secure handling of client credentials using environment variables
- User-friendly console and browser interactions

## Requirements

- Python 3.6 or higher
- PRAW
- python-dotenv

## Obtaining Reddit API Credentials

To use the script, you need to create a Reddit API application:

1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Fill in the details:
   - Name: Choose a name for your application
   - App type: Select "script"
   - Description: Optional
   - About url: Optional
   - Redirect uri: Set to `http://localhost:8080`
4. Click "Create app"
5. Note down the client ID (under the app name) and client secret

## Installation

1. Clone this repository or download the script files.

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the same directory as the script with the following content:

   ```
   CLIENT_ID=XXXX
   CLIENT_SECRET=XXXX
   REFRESH_TOKEN=XXXX
   REDIRECT_URI=http://localhost:8080
   SUBREDDIT=XXXX
   REFERRAL_CODE=XXXX
   ```

   Replace the placeholders with your actual information.

## Usage

### Authentication

1. Run the authentication script:

   ```
   python reddit_auth_script.py
   ```

2. The script will open a web browser window for you to log in to Reddit and authorise the application.

3. After authorisation, return to the terminal. The script will automatically complete the process and display your refresh token.

4. Add the refresh token to your `.env` file:

   ```
   REFRESH_TOKEN=your_refresh_token
   ```

### Posting Referral Code

1. After setting up authentication, run the main script:

   ```
   python main.py
   ```

2. The script will use the refresh token to authenticate and post your referral code to the specified subreddit.

## Logging

The script logs its actions and any errors to the specified log file (default: `reddit_bot.log`).

## Setting Up a Cron Job

To run the script automatically at regular intervals using cron:

1. Open your crontab configuration:

   ```
   crontab -e
   ```

2. Add a line to run the script every 24 hours (e.g., at midnight):

   ```
   0 0 * * * /usr/bin/python3 /path/to/main.py
   ```

3. Save and exit the crontab editor.
