from config import create_api
from datetime import date
import data
import tweepy
import matplotlib.pyplot as plt 

class Tweeter():
    """ Tweeter represents an object that has it's own
        Tweepy api and is given the ability to tweet
        given that api and some tweet (string) """

    def __init__(self):
        """ create_api comes from config.py and creates an api object """
        self.api = create_api();

    def tweet(self, tweet=''):
        """ Uses 'update_status' from tweepy to tweet """
        self.api.update_status(tweet)


def main():
    """ A main() that can be used as a script to tweet either
        1. new cases & total cases of a given day
        2. total cases of the most recent updated day """
    tweeter = Tweeter()
    # a dict of covid data with "MM/-D/YY" as keys
    covid_data = data.get_data()
    
    # get inner keys
    inner_keys = list(covid_data.values())[0].keys()

    # x-axis is the outer keys
    x_axis_values = list(map(str, covid_data.keys()))

    # loop through inner_keys
    for x in inner_keys:
        # create a list of values for inner key
        y_axis_values = [v[x] for v in covid_data.values()]

    # plot each inner key
    plt.plot(x_axis_values, y_axis_values, label=x)

    plt.legend()
    

if __name__ == '__main__':
    main()  


