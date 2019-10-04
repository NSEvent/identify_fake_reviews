# Podium Coding Challenge
“A Dealer For the People” by Kevin Tang

(Tested using Python 3.5.2)

## Prompt
The KGB has noticed a resurgence of overly excited reviews for a McKaig Chevrolet Buick, a dealership they have planted in the United States. In order to avoid attracting unwanted attention, you’ve been enlisted to scrape reviews for this dealership from DealerRater.com and uncover the top three worst offenders of these overly positive endorsements.

Your mission, should you choose to accept it, is to write a tool that:

- 1 scrapes the first five pages of reviews
- 2 identifies the top three most “overly positive” endorsements (using criteria of your choosing, documented in the README)
- 3 outputs these three reviews to the console, in order of severity

## "Overly positive" criteria
VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.

I chose to use VADER sentiment analysis for this task because it works well with online reviews, does not require training data, and is fast enough for our purposes. VADER sentiment analysis gives us a score for positive sentiment, which is the quantity I used for finding overly positive reviews. 

This program uses the average positive sentiment per sentence for each review to rank reviews.

## To setup:
### 1. Setup virtual env
```
python3 -m venv env
source env/bin/activate
```

### 2. Install pip packages
```
pip install -r requirements.txt
```

OR

```
pip install requests
pip install html5lib
pip install bs4
pip install nltk
```

### 3. Install nltk packages 
```
python3
>>> import nltk
>>> nltk.download('vader_lexicon')
```

## To run:
```
python3 find_fakes.py
```
