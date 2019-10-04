import requests
from bs4 import BeautifulSoup

# iterate through pages 1 through 5
# for i in range(1,6):
i = 1
url = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/' \
      'page{}/?filter=ALL_REVIEWS#link'.format(str(i))
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html5lib')
titles = soup.findAll('h3', attrs = {'class': 'no-format inline italic-bolder font-20 dark-grey'})
bodies = soup.findAll('p', attrs = {'class': 'font-16 review-content margin-bottom-none line-height-25'})

for title, body in zip(titles, bodies):
	print(title.text)
	print(body.text)

# print(title.text)
# print(body.text)

# 'no-format inline italic-bolder font-20 dark-grey'
# 'font-16 review-content margin-bottom-none line-height-25'
