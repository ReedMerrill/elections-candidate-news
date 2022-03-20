from requests_html import HTMLSession
import pandas as pd

# get names for search terms
df = pd.read_csv('ab2021_elec.csv', )

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

# make a url with each name in names as the search pattern on the news site
for name in names:

    # form url with name of candidate from list of names
    url = "https://calgaryherald.com/search/?search_text=" + name + "&date_range=" + timeframe + "&sort=score&from=0"

    response = session.get(url) # get response
    response.html.render()  # render javascript

    # initialize list for urls from the loop that iterates the name searches
    all_urls = []

    # loop over pages of search results
    for html in response.html:

        # get article url containers
        containers = response.html.find(selector='.article-card__link')

        # isolate the hrefs from the container list items
        containers = [str(container) for container in containers] # convert list elements to string, cause who know what they were before this
        hrefs = [container.split("href='")[1] for container in containers] # split the hrefs out of the class and select the 1st element (the href, not the string before the split pattern
        hrefs = [href[0:len(href)-2] for href in hrefs] # clean trailing characters from hrefs

        # create article urls
        urls_single_search = ['https://calgaryherald.com' + href for href in hrefs]

    all_urls = all_urls + urls_single_search
