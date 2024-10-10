import praw
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from dotenv import load_dotenv
import os
import sys
import logging
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

def create_reddit_instance():
    try:
        return praw.Reddit(
            client_id=os.getenv('CLIENT_ID'),
            client_secret=os.getenv('CLIENT_SECRET'),
            redirect_uri=os.getenv('REDIRECT_URI'),
            user_agent='Reddit Referral Code Poster (by u/impshum)'
        )
    except praw.exceptions.PRAWException as e:
        logging.error(f"Error creating Reddit instance: {e}")
        sys.exit(1)

class RedditAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse.urlparse(self.path)
        query_params = urlparse.parse_qs(parsed_url.query)

        if 'code' in query_params:
            code = query_params['code'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
            <html>
            <body>
                <h1>Authorization successful!</h1>
                <p>You can now close this window. The process will continue in the terminal.</p>
            </body>
            </html>
            """)
            logging.info(f"Authorization code received: {code}")

            try:
                refresh_token = self.server.reddit.auth.authorize(code)
                logging.info(f"Refresh Token: {refresh_token}")
                self.server.refresh_token = refresh_token
            except praw.exceptions.OAuthException as e:
                logging.error(f"OAuth Error: {e}")

            threading.Thread(target=self.server.shutdown).start()
        else:
            self.send_error(400, "Missing authorization code")

    def log_message(self, format, *args):
        return

def main():
    reddit = create_reddit_instance()

    auth_url = reddit.auth.url(
        scopes=["identity", "read", "submit"],
        state="random_state_string",
        duration="permanent"
    )

    print("\nPlease open the following URL in your web browser to authorize the application:")
    print(f"\n{auth_url}\n")
    print("After you've authorized the application, the process will continue automatically.")

    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RedditAuthHandler)
    httpd.reddit = reddit
    httpd.refresh_token = None

    logging.info("Waiting for authorization...")
    httpd.serve_forever()

    refresh_token = httpd.refresh_token
    httpd.server_close()

    if refresh_token:
        logging.info("Authentication successful!")
        print(f"\nYour refresh token is: {refresh_token}")
        print("You can now use this refresh token for future authentications.")
        print("Add this to your .env file as REFRESH_TOKEN=your_refresh_token")
    else:
        logging.error("Failed to obtain refresh token.")

    return refresh_token

if __name__ == '__main__':
    main()
