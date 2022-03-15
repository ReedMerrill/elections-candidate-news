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

# get urls to give to newspaper3k
containers = response.html.find('.article-card__link')

# isolate the hrefs from the container list items

# Grab url of each the article
base = 'https://calgaryherald.com'
href = response.html.xpath('/html/body/main/div/div/div[2]/div/article[1]/div/div/a/@href')[0]
article_url = base + href
# follow article link
article_response = session.get(article_url)
article_response.html.render()
# get article date
date = article_response.html.xpath('/html/body/main/article/header/div/div[2]/span')[1].text
# get main article text
len(article_response.html.find('.article-content__content-group'))