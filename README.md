# Bobby B Bot - Reddit version
[![Build Status](https://travis-ci.org/bobby-b-bot/reddit.svg?branch=master)](https://travis-ci.org/bobby-b-bot/reddit) ![GitHub release](https://img.shields.io/github/release/bobby-b-bot/reddit.svg) ![GitHub All Releases](https://img.shields.io/github/downloads/bobby-b-bot/reddit/total.svg) ![GitHub issues](https://img.shields.io/github/issues-raw/bobby-b-bot/reddit.svg) ![GitHub](https://img.shields.io/github/license/bobby-b-bot/reddit.svg) ![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/bobby_b_bot.svg?style=social) [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/L3L814HD5)


In this repository you can find the Reddit (and original) version of the Bobby B Bot.

## How to use it

Simply write one of the [keywords](https://github.com/bobby-b-bot/utils/blob/master/triggers.json) (usually variations of the bot's name) in a comment in the [subreddits](subs.json) the bot is listening on, and the bot will reply with a random quote.

* Only listens on mentioned subreddits to avoid spamming other subs. 
* Always follow and comply with Reddit bot rules and best practices: [bottiquette](https://www.reddit.com/r/Bottiquette/wiki/bottiquette)

## How to install

1. Create a virtual environment and activate it (this is optional but when working with Python, I cannot recommend it enough) or create a root folder that will hold all the code;
2. Clone reddit repository inside this virtual enviroment folder (let's call it 'root') and then clone [utils](https://github.com/bobby-b-bot/utils.git) repository. The final structure should be somewhat similar to this:

```
+ root
└───+ reddit
│     |-- praw.ini 
│     |-- blocked_users.json
│     |-- subs.json
│     |-- reddit_bot.py
└───+ utils
      |-- __init__.py
      |-- core.py
      |-- logging_config.ini
      |-- quotes.json
      |-- triggers.json
```

4. Run command `pip install -r requirements.txt` in reddit directory (this should install the requirements for utils as well, otherwise, you can also run the command in utils folder);
5. Done, you are ready to configure it.

#### TL;DR Installation:

```
$ python -m venv <venv_name>
$ cd venv_name
$ source bin/activate
(venv_name) $ git clone https://github.com/bobby-b-bot/reddit.git
(venv_name) $ git clone https://github.com/bobby-b-bot/utils.git
(venv_name) $ cd reddit
(venv_name) $ pip install -r requirements.txt
```

## How to configure and run

1. Create and maintain the .env file for environment variables in reddit folder (ENV = 'TEST' or 'PROD' and TST_SUBS);
1. Create and maintain the praw.ini file for PRAW (Python Reddit API) in root reddit folder ([see PRAW documentation](https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html));
1. Create and mantain a logging_config.ini file in utils folder for logging configuration ([see documentation](https://docs.python.org/3/library/logging.config.html#logging-config-fileformat));
1. Run the bot (`python reddit_bot.py`).
1. Have fun!

## How to contribute

Feature requests such as new quotes or more subreddits to run the bot on are welcome via issues on GitHub! Feel free to contribute. You can also contribute by donating via [![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/L3L814HD5) or [PayPal](http://paypal.me/felipezanettini) to keep the servers running. 
