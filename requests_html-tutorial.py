from requests_html import HTMLSession
session = HTMLSession()
r = session.get('https://python.org/')

# grab links from the page
r.html.links

# get absolute links (including anchors)
r.html.absolute_links

# use a CSS selector
about = r.html.find('#about', first=True)

# Grab an element's text contents
print(about.text)

# introspect and element's attributes:
about.attrs

# render an element's HTML
about.html
r.html.search(