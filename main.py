# get webpages
from requests import *
from requests_html import HTMLSession

# define url
search_terms = "municipal+election"
timeframe = "-365d"
page = "0"
url = "https://calgaryherald.com/search/?search_text="+search_terms+"&date_range="+timeframe+"&sort=score&from="+page

# get the webpage
session = HTMLSession()
response = session.get(url)
response.html.render() # render javascript

urls_out = []
for html in response.html:

    # get article url containers
    containers = response.html.find(selector='.article-card__link')

    # isolate the hrefs from the container list items
    containers = [str(container) for container in containers] # convert list elements to string, cause who know what they were before this
    hrefs = [container.split("href='")[1] for container in containers] # split the hrefs out of the class and select the 1th element (the href, not the string before the split pattern
    hrefs = [href[0:len(href)-2] for href in hrefs] # clean trailing characters from hrefs

    # create article urls
    urls = ['https://calgaryherald.com'+href for href in hrefs]

    return urls_out = urls_out + urls