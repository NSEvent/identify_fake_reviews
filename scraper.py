import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('vader_lexicon')
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Review:
	def __init__(self, title, body, score):
		self.title = title
		self.body = body
		self.score = score

	def __str__(self):
		return 'Title: {}Body: {}Score: {}\n'

	def __gt__(self, other):
		return self.score > other.score


top_scores = list(0,0,0)
top_titles = list('','','')
top_bodies = ('','','')

# iterate through pages 1 through 5
for i in range(1,6):
	url = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/' \
	      'page{}/?filter=ALL_REVIEWS#link'.format(str(i))
	req = requests.get(url)

	# use BeautifulSoup to make html parse tree, grab all reviews on the page
	soup = BeautifulSoup(req.content, 'html5lib')
	titles = soup.findAll('h3', attrs = {'class': 'no-format inline italic-bolder font-20 dark-grey'})
	bodies = soup.findAll('p', attrs = {'class': 'font-16 review-content margin-bottom-none line-height-25'})

	senti = SentimentIntensityAnalyzer()

	for title, body in zip(titles, bodies):
		all_text = title.text + body.text

		sentence_score = 0 # will be average positive sentiment per sentence in the title + body
		sentences = tokenize.sent_tokenize(all_text)
		for sentence in sentences:
			score = senti.polarity_scores(sentence)
			sentence_score += score['pos']
		sentence_score = sentence_score / len(sentences)

		if sentence_score > top_scores[2]



	# scores = senti.polarity_scores(all_text)
	# print(scores['compound'])


	# for k in scores:
	# 	print('{0}: {1}, '.format(k, scores[k]), end='')

# print(title.text)
# print(body.text)

# 'no-format inline italic-bolder font-20 dark-grey'
# 'font-16 review-content margin-bottom-none line-height-25'
