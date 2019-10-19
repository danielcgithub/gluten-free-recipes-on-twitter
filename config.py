import tweepy
import logging
import os
import configparser

logger = logging.getLogger()


def create_api():

    config = configparser.ConfigParser()
    config.read("secrets.ini")
    consumer_key = config.get("secrets", "consumer_key")
    consumer_secret = config.get("secrets", "consumer_secret")
    access_token = config.get("secrets", "access_token")
    access_token_secret = config.get("secrets", "access_token_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
