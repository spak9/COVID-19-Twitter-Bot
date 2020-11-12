from config import create_api
from datetime import date
import data
import tweepy
import time


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
    i = 1
    county = 'Fairfax County'
    
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
    
    # loop and do basic tweeting of the covid metrics
    # every 2 minutes
    while True:
        # a dict of covid data with "MM/-D/YY" as keys
        covid_data = data.get_data()
        today = date.today().strftime("%-m/%-d/%y")

        # check if there is data for today
        if today in covid_data:
            new_cases_today = covid_data[today]['new_cases']
            known_cases = covid_data[today]['known_cases']
            tweeter.tweet(
                f'{today}: New COVID-19 Cases in {county}: {new_cases_today}\n'
                f'Total COVID-19 Cases in Fairfax County: {known_cases}\n'
                f'{i}/24')
            print('Tweet Successful')
        # old data
        else:
            today = list(covid_data.keys())[0]
            known_cases = covid_data[today]['known_cases']
            tweeter.tweet(f'{today}: Total COVID-19 Cases in {county}: {known_cases}\n'
                f'{i}/24')
            print('Tweet Successful')

        # some counter to make sure we don't repeat tweets --> error
        i = i + 1
        if (i > 24): i = 1

        # sleep to only tweet every hour
        time.sleep(3600)


if __name__ == '__main__':
    main()
