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
    """ A main() that will loop every minute to listen to replies
        and every hour to tweet basic metrics solely on 'Fairfax County' """

    tweeter = Tweeter()
    # a basic counter to make sure that our tweets are all 'unique'
    i = 1
    # an hour counter to tweet 'Fairfax County' metric every hour
    hour_keeper = 1
    # every tweet has a unique tweet id
    since_id = 1
    county = 'Fairfax County'

    # 1st loop is for hourly tweeting
    while True:
        # 2nd loop is to listen every minute for new replies
        while True:
            since_id = mention_reply(tweeter, since_id, i)
            print('since_id', since_id)
            hour_keeper += 1
            # if we reach an hour, reset
            if (hour_keeper == 60):
                hour_keeper = 1
                break
            else: time.sleep(60)
            i += 1
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
        if (i > 1440): i = 1

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
                return since_id

            # check if there is data for today
            if today in covid_data:
                new_cases_today = covid_data[today]['new_cases']
                known_cases = covid_data[today]['known_cases']
                tweeter.api.update_status(
                    status=f'{today}: New COVID-19 Cases in {county}: {new_cases_today}\n'
                    f'Total COVID-19 Cases in {county}: {known_cases}. {i}/1440\n',
                    in_reply_to_status_id=tweet.id)
                print('Tweet Successful')
            # old data
            else:
                today = list(covid_data.keys())[0]
                known_cases = covid_data[today]['known_cases']
                tweeter.api.update_status(
                status=f'{today}: Total COVID-19 Cases in {county}: {known_cases}. {i}/1440\n',
                in_reply_to_status_id=tweet.id)
                print('Tweet Successful')

        return new_since_id


if __name__ == '__main__':
    main()
