# a configuration file to bootstrap the creation of
# a Tweepy.API object

import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    # typically stores the keys in a more secure environment, but
    # for our sake, we'll just keep it in this file for now
    consumer_key = "DMbjxaGdJOBqYevWziViqSden"
    consumer_secret = "7dp54lFGsBGU3nn98eCTyCQPuPvQn9fSQ3nXodKMjpnT4Gv6gy"
    access_token = "1307135381549187072-PO7zJQurXQAFxY7GciEqIOPxaBp14T"
    access_token_secret = "0YQEN2IDk7KutAMMvNz3WpF0IFmXAyrFef6QWjlrWKN8T"

    # Tweepy offers 'OAuthHandler' class to handle the OAuth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # The two kwarg arguments makes Tweepy wait & notify us when we
    # reach out tweet limit
    # 'api' object itself is a wrapper for the Twitter api
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        # will verify & return User object if valid, false otherwise
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
