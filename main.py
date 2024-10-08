import praw
import logging
from dotenv import load_dotenv
import os

load_dotenv()

def create_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        user_agent=os.getenv('USER_AGENT'),
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD')
    )

def post_to_reddit(reddit, subreddit_name, title):
    try:
        reddit.subreddit(subreddit_name).submit(title)
        logging.info(f"Posted referral code to r/{subreddit_name}: {title}")
    except praw.exceptions.RedditAPIException as e:
        logging.error(f"Reddit API error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    else:
        logging.info("Post submitted successfully.")
    finally:
        logging.info("Finished attempting to post.")

def main():
    logging.basicConfig(
        filename=os.getenv('LOG_FILE'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    reddit = create_reddit_instance()
    post_to_reddit(reddit, os.getenv('SUBREDDIT'), os.getenv('REFERRAL_CODE'))

if __name__ == "__main__":
    main()
