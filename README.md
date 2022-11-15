## PokeReddit Bot
A reddit bot designed to track information on the r/Pokemon subreddit.

### Setup
This project requires several steps to begin using. You will need a working [Reddit](https://www.reddit.com/) account, and to create a [script-application](https://www.reddit.com/prefs/apps) in this account. Once complete, I recommend following PRAW's [instructions](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#oauth) to get started.

### Purpose
This bot is meant to pull data from the Reddit API via PRAW and analyze the results.

Currently it is designed to iterate through all comments and posts on r/pokemon from the previous 24 hours looking for mentions of the original 151 pokemon. It tallies these mentions, and outputs a dictionary with the results.

In the future I plan to add more features such as spacy sentiment-analysis, and results storage.
