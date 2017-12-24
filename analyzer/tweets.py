#!/usr/bin/env python3

import os
import sys
import nltk

from analyzer import Analyzer
from termcolor import colored
from helpers import get_user_timeline
from nltk.tokenize import TweetTokenizer


def main():

    # ensure proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: ./tweet @screen_name")

    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # get user's tweets and instatiate TweetTokenizer class
    tweets = get_user_timeline(sys.argv[1], count=50)
    t = TweetTokenizer()

    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # analyze word
    for tweet in tweets:
        score = analyzer.analyze(t.tokenize(tweet))
        if score > 0.0:
            print()
            print(colored(":)", "green"), end=" ")
            print(tweet)
        elif score < 0.0:
            print()
            print(colored(":(", "red"), end=" ")
            print(tweet)
        else:
            print()
            print(colored(":|", "yellow"), end=" ")
            print(tweet)

if __name__ == "__main__":
    main()