# Bobby B Bot - Reddit version

In this repository you can find the Reddit (and original) version of the Bobby B Bot.

## How to use it

Simply write one of the [keywords](https://github.com/bobby-b-bot/utils/blob/master/triggers.json) (usually variations of the bot's name) in a comment in the [subreddits](subs.json) the bot is listening on, and the bot will reply with a random quote.

* Only listens on mentioned subreddits to avoid spamming other subs. 

## How to install

1. Create a virtual environment and activate it (this is optional but when working with Python, I cannot recommend it enough) or create a root folder;
2. Clone reddit repository inside this virtual enviroment folder (let's call it 'root'). The final structure should be somewhat similar to this:
```
root
│    
│
└───reddit
    │   praw.ini 
    │   blocked_users.json
    │   subs.json
    │   reddit_bot.py
    │
    └───utils
        │   __init__.py
        │   core.py
        │   logging_config.ini
        │   quotes.json
        │   triggers.json
```
4. Run command `pip install -r requirements.txt` in reddit directory (this should clone the utils repo and install the requirements for utils as well, otherwise, you can also run the command in utils folder);
5. Create and maintain the .env file for environment variables in reddit folder (ENV = 'TEST' or 'PROD' and TST_SUBS);
6. Create and maintain the praw.ini file for PRAW (Python Reddit API) in root reddit folder ([see PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html));
7. Create and mantain a logging_config.ini file in utils folder for logging configuration ([see documentation](https://docs.python.org/3/library/logging.config.html#logging-config-fileformat));
8. Run the bot (`python reddit_bot.py`).

## How to contribute 
Feature requests such as new quotes or more subreddits to run the bot on are welcome! Feel free to contribute. You can also contribute by donating via [PayPal](http://paypal.me/felipezanettini) to keep the servers running. 
