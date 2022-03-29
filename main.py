from requests_html import HTMLSession
import time
import pandas as pd

# get names for search terms
df = pd.read_csv('ab2021_elec.csv')

# filter to Calgary only
calgary = df[df.municipality.eq('Calgary')]

# combine first and last name into one column
names = calgary['first_name'] + '+' + calgary['last_name']

# replace chars that break the url
names = names.tolist()
names = [name.replace(" ", "+").replace("(", "").replace(")", "").replace("'", "%27") for name in names]

# define url
timeframe = "-365d"

# get the webpage
session = HTMLSession()

# initialize list for urls from the loop that iterates the name searches
candidate_urls = []

names = ['Ian+Chiang', 'Jan Damery']

# make a url with each name in names as the search pattern on the news site
for name in names:

    # form url with name of candidate from list of names
    url = "https://calgaryherald.com/search/?search_text=" + name + "&date_range=" + timeframe + "&sort=score&from=0"

    response = session.get(url) # get response
    response.html.render()  # render javascript

    candidate_urls += response

    print("First search page for " + name.replace("+", " ") + " is saved.")

    time.sleep(3)

