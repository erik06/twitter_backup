import tweepy
import os
import csv
import json
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("TW_API_KEY")
consumer_secret = os.getenv("TW_API_KEY_SECRET")
access_key = os.getenv("TW_ACCESS_TOKEN")
access_secret = os.getenv("TW_ACCESS_TOKEN_SECRET")


def get_all_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(
        screen_name=screen_name, count=200, tweet_mode="extended"
    )

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print(f"getting tweets before {oldest}")

        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(
            screen_name=screen_name, count=200, max_id=oldest, tweet_mode="extended"
        )

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print(f"...{len(alltweets)} tweets downloaded so far")

    with open("alltweets.json", "a", encoding="utf-8") as f:
        f.writelines('{"tweets":[')
        for tweet in alltweets:
            if tweet._json:
                f.write(json.dumps(tweet._json))
                f.write(",\n")
        f.writelines("]}")


if __name__ == "__main__":
    # pass in the username of the account you want to download
    username = os.getenv("TW_USERNAME")
    get_all_tweets(username)
