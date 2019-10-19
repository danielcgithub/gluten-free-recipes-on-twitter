import tweepy
import logging
from config import create_api
import json


def main():
    api = create_api()
    tweets = api.favorites()

    for tweet in tweets:
        print(f"unliking and unretweeting tweet {tweet.id}")
        api.destroy_favorite(tweet.id)
        api.unretweet(tweet.id)


if __name__ == "__main__":
    main()
