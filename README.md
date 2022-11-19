# Requirements

- Python 3.9+
- Pipenv

This application uses tweepy. [Tweepy Docs](https://docs.tweepy.org/en/stable/).

## Installation

- Run `pipenv install`

Add a `.env` file in the root of the application and fill in the required missing elements from your own Twitter application.

[Twitter application registration](https://developer.twitter.com/en/portal/projects-and-apps)

```bash
TW_ACCESS_TOKEN=" "
TW_ACCESS_TOKEN_SECRET=" "
TW_API_KEY=" "
TW_API_KEY_SECRET=" "
TW_USERNAME=" "
```

Where `TW_USERNAME` is the twitter username (**without** the @ symbol in front) you want to receive.

## Running the application

- After all installs run `pipenv run python app.py`
- Check the root for the newly created `alltweets.json` file which contains all your tweets

## Improvement ideas

- Download media (images etc)
- Replace t.co URLs with full expanded URLs
- Create a sample HTML website from tweets
  - Put each tweet in it's own folder/directory named after the tweet id number
  - Create an index page to browse the tweets
- Consider combining with Hugo to create a full static site of tweet backups
