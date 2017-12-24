# Complete the implementation of main in tweets in such a way that program

# accepts one and only one command-line argument, the screen name for a user on Twitter,

# queries Twitter’s API for a user’s most recent 50 tweets,

# analyzes the sentiment of each of those tweets, and

# outputs each tweet’s score and text, colored in green if positive, red if negative, and yellow otherwise.

# TODO
# ensure proper usage
#  look at smile
# get tweets
#  helpers.py
#    get_user_timeline
#  check if successful
#		 (what does the function return if failed)
#  error message if unsuccessful
#    sys.exit
#  user TweetTokenizer in nltk
# initialize Analyzer
# analyze tweets