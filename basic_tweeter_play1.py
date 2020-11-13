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
    
    # a dict of covid data with "MM/-D/YY" as keys
    covid_data = data.get_data()
    
    #resizing the figure
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 20
    fig_size[1] = 10
    plt.rcParams["figure.figsize"] = fig_size
    

    # get inner keys of new cases
    inner_keys = list(covid_data.values())[0].keys()

    # x-axis is the outer keys
    x_axis_values = list(map(str, covid_data.keys()))

    # loop through inner_keys
    for x in inner_keys:
        # create a list of values for inner key
        y_axis_values = [v[x] for v in covid_data.values()]
  

    #get inner keys of known cases
    inner_keys2=sorted(list(covid_data.values())[0].keys(), reverse=True)
       
    # loop through inner_keys
    for z in inner_keys2:
        # create a list of values for inner key
        y_axis_values2 = [v[z] for v in covid_data.values()]

    #creating separate plots for new cases and known cases and saving the figs in directory.
    plt.subplot(2,2,1)
    plt.plot(x_axis_values, y_axis_values, 'b*-')
    plt.title("new cases")
    plt.subplot(2,2,2)
    plt.plot(x_axis_values, y_axis_values2, 'y--')
    plt.title("known cases")
    plt.savefig("cases.png")


if __name__ == '__main__':
    main()  


