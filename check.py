# Authenticate to Twitter
# Find the keys on "https://developer.twitter.com/en/portal/apps/18908512/keys"
import tweepy
auth = tweepy.OAuthHandler("DMbjxaGdJOBqYevWziViqSden",
    "7dp54lFGsBGU3nn98eCTyCQPuPvQn9fSQ3nXodKMjpnT4Gv6gy")
auth.set_access_token("1307135381549187072-JDXgwcVYTDIpzxjcPZ3nGg4BRLHjfA",
    "UssQEqvpYHe3l3wFYDQ37TjBMajWANljRXqC439xiJvDY")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
