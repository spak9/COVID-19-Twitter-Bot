import requests
import csv
import json
from datetime import date, timedelta

url = 'https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv'

past_week_dates = [(date.today() - timedelta(days=t)) for t in range(2, 10)]

# format date objects as strings in the form "10/5/20"
# this is the format used by USAFacts data
past_week_keys = [d.strftime("%-m/%-d/%y") for d in past_week_dates]

def parse_row(row):
    result = {}
    for i in range(len(past_week_keys)-1):
        current_date = past_week_keys[i]
        previous_date = past_week_keys[i+1]
        result[current_date] = {
            'known_cases': int(row[current_date]),
            # today's cases - yesterday's cases = new cases
            # not exactly true since this could be negative if known cases decreases
            'new_cases':   int(row[current_date]) - int(row[previous_date])
        }
    return result


def get_data(county='Fairfax County'):
    response = requests.get(url)
    reader = csv.DictReader(response.text.splitlines())
    covid_data = {}
    for row in reader:
        # if county exists in the data
        if row['County Name'] == county:
            covid_data = parse_row(row)
            print(json.dumps(covid_data))
            break
        # else it doesn't; will return an empty dictionary
    return covid_data

if __name__ == '__main__':
    get_data()
