# Standard library imports
import re
import time
import datetime
import json
import os.path
import logging
from logging.config import fileConfig

# Third party imports
import praw
from prawcore.exceptions import PrawcoreException as APIException # PRAW API exception handlers
import praw.exceptions

# Local application imports
from utils.core import get_env, get_username, is_keyword_mentioned, get_random_quote # bot standard functions

# validate all mandatory files exist before starting
assert os.path.isfile('../utils/logging_config.ini') # Logs config file
assert os.path.isfile('praw.ini')                   # PRAW config file
assert os.path.isfile('.env')                       # environment variables file
assert os.path.isfile('subs.json')                  # subreddits file
assert os.path.isfile('blocked_users.json')         # blocked users file

if not os.path.isfile('posts_replied_to.txt'):      # If record file does not exist create it
    open("posts_replied_to.txt", "w+")

# Instantiate logging in accordance with config file
fileConfig('../utils/logging_config.ini')
logger = logging.getLogger('reddit')

# Explicit start of the bot runtime
logger.info("Started Reddit bot")

try:
    # Check if it is PROD or TEST environment, which changes the variables such as subreddits
    environment = get_env('ENV', __file__)
    logger.info("Running on environment: {}".format(environment))

    with open('subs.json', 'r') as subs:

        if environment == 'TEST':
            # test sub is in environment variables
            subreddits = get_env('TST_SUBS', __file__)
        elif environment == 'PROD':
            # productive subs are on a JSON file
            json_raw = json.load(subs)
            subreddits = '+'.join(json_raw)
        else:
            raise Exception # invalid environment variable

    logger.info("Got subreddit names: bot running on {} subreddits".format(subreddits.count('+') + 1)) # count '+' sign plus one.
except Exception as e:
    logger.exception("Could not get environment variables: {}".format(str(vars(e))))

# Do not reply to comments from these users
with open('blocked_users.json', 'r') as blocked_users:
    users_list = json.load(blocked_users)
logger.info("Loaded blocked users list: {} users".format(len(users_list)))

if __name__ == '__main__':
    while True:
        try:
            # Create the Reddit instance
            reddit = praw.Reddit('bot1')
            logger.info("Instantiated Reddit client")

            # Read the file into a list and remove any empty values
            with open("posts_replied_to.txt", "r") as f:
                posts_replied_to = f.read()
                posts_replied_to = posts_replied_to.split("\n")
                posts_replied_to = list(filter(None, posts_replied_to))
                logger.info("Got posts that were already replied")
                    
            # Get the replies from the subreddits
            subreddit = reddit.subreddit(subreddits)

            for comment in subreddit.stream.comments():

                # Check if author name exists or not
                username = get_username(comment.author)
                
                # If we haven't replied to this comment before and the comment author is not blocked
                if comment.id not in posts_replied_to and username not in users_list:
                    
                    if is_keyword_mentioned(comment.body):

                        # Reply to the post and write activity to the log
                        comment.reply(get_random_quote())
                        logger.info("Replied to comment in subreddit '{}'".format(comment.subreddit))

                        # Store the current id into our list
                        posts_replied_to.append(comment.id)
                        logger.info("Appended replied posts to list")
                        
                        # Write our updated list back to the posts_replied_to.txt file and to the log
                        with open("posts_replied_to.txt", "a") as f:
                            f.write(comment.id + "\n")
                        logger.info("Written to 'posts_replied_to.txt' file, ID '{}'".format(comment.id))
                            
        except KeyboardInterrupt:
            logger.error("Keyboard termination received. Bye!")
            break
        except APIException as e:
            logger.exception("PRAW Exception received: {}. Retrying...".format(str(vars(e))))
            time.sleep(2) # sleep to retry in case of errors
