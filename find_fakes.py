# Podium Coding Challenge
# Kevin Tang
# 10/3/2019

import requests
from bs4 import BeautifulSoup
import nltk
# nltk.download('vader_lexicon')
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Review:
	def __init__(self, title, body, score):
		self.title = title
		self.body = body
		self.score = score

	def __str__(self):
		return 'Title: {}\nBody: {}\nScore: {}\n'.format(self.title, self.body, self.score)

	def __gt__(self, other):
		return self.score > other.score

	def __ge__(self, other):
		return self.score >= other.score

def main():
	reviews = list()

	# iterate through pages 1 through 5
	for i in range(1,6):
		url = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/' \
		      'page{}/?filter=ALL_REVIEWS#link'.format(str(i))

		# attempt GET request
		try:
			req = requests.get(url)
		except requests.exceptions.RequestException as e:
			print(e)
			sys.exit(1)

		# use BeautifulSoup to make html parse tree, grab all reviews on the page
		soup = BeautifulSoup(req.content, 'html5lib')
		titles = soup.findAll('h3', attrs = {'class': 'no-format inline italic-bolder font-20 dark-grey'})
		bodies = soup.findAll('p', attrs = {'class': 'font-16 review-content margin-bottom-none line-height-25'})

		senti = SentimentIntensityAnalyzer()

		# iterate through the reviews on the current page
		for title, body in zip(titles, bodies):
			all_text = title.text + body.text

			sentence_score = 0 # will be average positive sentiment per sentence in the title + body
			sentences = tokenize.sent_tokenize(all_text)
			for sentence in sentences:
				score = senti.polarity_scores(sentence)
				sentence_score += score['pos']
			sentence_score = sentence_score / (len(sentences) + 1)

			# store Review in list
			reviews.append(Review(title.text, body.text, sentence_score))

	# can use partial sort to make this faster, especially when looking at more reviews
	reviews.sort(reverse=True)

	for i in range(0,3):
		print(reviews[i])

if __name__== "__main__":
  main()
