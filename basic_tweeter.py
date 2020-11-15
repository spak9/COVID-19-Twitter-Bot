from config import create_api
from datetime import date
import matplotlib.pyplot as plt
import data
import tweepy
import time


class Tweeter():
    """ Tweeter represents an object that has it's own
        Tweepy api and is given the ability to tweet
        given that api and some tweet (string) """

    # a class variable to hold the list of 24 counties in Virginia
    counties = [
        'Accomack County', 'Albemarle County', 'Alleghany County',
        'Amelia County', 'Amherst County', 'Appomattox County',
        'Appomattox County', 'Augusta County', 'Bath County',
        'Bedford County', 'Bland County', 'Botetourt County',
        'Brunswick County', 'Buchanan County', 'Buckingham County',
        'Campbell County', 'Caroline County', 'Carroll County',
        'Charles City County', 'Charlotte County', 'Fairfax County',
        'Essex County', 'Halifax County', 'Henrico County'
    ]

    def __init__(self):
        """ create_api comes from config.py and creates an api object """
        self.api = create_api();

    def tweet(self, tweet=''):
        """ Uses 'update_status' from tweepy to tweet """
        self.api.update_status(tweet)


def main():
    """ A main() that will loop every minute to listen to replies
        and every hour to tweet basic metrics solely on 'Fairfax County' """

    tweeter = Tweeter()
    county = 'Fairfax County'
    # a basic counter to make sure that our tweets are all 'unique'
    i = 0

    # 1st loop is for hourly tweeting
    while True:
        # iterate through 24 counties
        county = tweeter.counties[i]
        covid_data = data.get_data(county=county)
        today = date.today().strftime("%-m/%-d/%y")

        # check if there is data for today
        if today in covid_data:
            new_cases_today = covid_data[today]['new_cases']
            known_cases = covid_data[today]['known_cases']
            get_graph(covid_data, i)
            media = tweeter.api.media_upload(f'case_{i}.png')
            tweeter.api.update_status(
                status=f'{today}: New COVID-19 Cases in {county}: {new_cases_today}\n'
                f'Total COVID-19 Cases in Fairfax County: {known_cases}\n'
                f'{i}/24',
                media_ids=[media.media_id])
            print('Tweet Successful')
        # old data
        else:
            today = list(covid_data.keys())[0]
            known_cases = covid_data[today]['known_cases']
            get_graph(covid_data, i)
            media = tweeter.api.media_upload(f'case_{i}.png')
            tweeter.api.update_status(
                status=f'{today}: Total COVID-19 Cases in {county}: {known_cases}\n'
                f'{i}/24',
                media_ids=[media.media_id])
            print('Tweet Successful')

        # some counter to make sure we don't repeat tweets --> error
        time.sleep(3600)
        i = i + 1
        # once we hit the 24 counties, reset it
        if (i > 23): i = 0

# Not implemented in bot
def mention_reply(tweeter, since_id, i):
    """ 'mention_reply' will check our twitter account for specific replies of
    the form: 'County_name County' and if the reply passes, reply back with
    basic covid metric """

    new_since_id = since_id
    user_name = '@COVID_Updater'
    mentions = tweepy.Cursor(tweeter.api.search, q=f'to:{user_name}', since_id=since_id).items()
    # if there are no mentions, exit
    if (True):
        print('Entering mention_reply')
        # iterate through all the replies since 'since_id'
        for tweet in mentions:
            # if some reply's id is less than or equal the current 'since_id',
            # then we know that we've seen it and don't want to reply
            if (tweet.id <= since_id): return since_id

            new_since_id = max(tweet.id, new_since_id)
            # the text of the tweet
            text = tweet.text
            print(text)
            # format it correctly; uppercase letter on word
            text = text.lower()
            # changes 'fairfax county' to 'Fairfax County'
            county = ' '.join([token[0].upper() + token[1:] for token in text.split()])
            print('County: ', county)
            covid_data = data.get_data(county=county)
            today = date.today().strftime("%-m/%-d/%y")

            # county doesn't exist or incorrectly formattted
            if not covid_data:
                print('Dictionary not valid')
                tweeter.api.update_status(
                    status=f'Sorry, either county does not exist or reply was misformatted. Is it in the format: County_name County?',
                    in_reply_to_status_id=tweet.id
                )
                return new_since_id

            # check if there is data for today
            if today in covid_data:
                new_cases_today = covid_data[today]['new_cases']
                known_cases = covid_data[today]['known_cases']
                tweeter.api.update_status(
                    status=f'{today}: New COVID-19 Cases in {county}: {new_cases_today}\n'
                    f'Total COVID-19 Cases in {county}: {known_cases}. {i}/1440\n',
                    in_reply_to_status_id=tweet.id)
                # call get_graph
                get_graph(covid_data)
                print('Tweet Successful')
            # old data
            else:
                today = list(covid_data.keys())[0]
                known_cases = covid_data[today]['known_cases']
                tweeter.api.update_status(
                status=f'{today}: Total COVID-19 Cases in {county}: {known_cases}. {i}/1440\n',
                in_reply_to_status_id=tweet.id)
                # call get_graph
                get_graph(covid_data)
                print('Tweet Successful')

        return new_since_id

def get_graph(covid_data, i):

    #resizing the figure
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 15
    fig_size[1] = 14
    plt.rcParams["figure.figsize"] = fig_size


    # get inner keys of new cases
    new_cases_keys = list(covid_data.values())[0].keys()

    # x-axis is the outer keys
    x_axis_values = list(map(str, covid_data.keys()))

    # loop through inner_keys
    for x in new_cases_keys:
        # create a list of values for inner key
        y_axis_values = [v[x] for v in covid_data.values()]


    #get inner keys of known cases
    known_cases_keys=sorted(list(covid_data.values())[0].keys(), reverse=True)

    # loop through inner_keys
    for z in known_cases_keys:
        # create a list of values for inner key
        y_axis_values2 = [v[z] for v in covid_data.values()]

    #creating separate plots for new cases and known cases and saving the figs in directory.
    plt.subplot(2,2,2)
    plt.plot(x_axis_values, y_axis_values2, 'y--')
    az=plt.gca()
    az.invert_xaxis()
    plt.title("known cases")

    plt.subplot(2,2,1)
    plt.plot(x_axis_values, y_axis_values, 'b*-')
    ax=plt.gca()
    ax.invert_xaxis()
    plt.title("new cases")
    plt.savefig(f'case_{i}.png')


if __name__ == '__main__':
    main()
