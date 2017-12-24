
from nltk.tokenize import TweetTokenizer
# from twython import Twython, TwythonError
# import class Twython, and exception class TwythonError

# t = Twython('ERssaG6yWs2rdNMAUlFN3nWUv', 'ZccVNHJRoQoumLtFBpT8oz6vjWyGnS7b2kxyuNm7vQ7TFMZTIa')

# results = t.search(q='katyperry', count=5)

# all_tweets = results['statuses']

# for tweet in all_tweets:
# 	print(tweet['text'])

text = "@katyperry this is a tweet #cool #whatwhat"
t = TweetTokenizer()
tokens = t.tokenize(text)
print(tokens)