import nltk
# nltk.download('punkt')
from nltk.tokenize import word_tokenize

class Analyzer():
    """Implements sentiment analysis."""
   
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = set([])
        self.negatives = set([])

        with open(positives, "r") as file:
            for line in file:
                if (line.startswith(';') == False) and (line.startswith('\n') == False):
                    self.positives.add(line.strip())

        with open(negatives, "r") as file:
            for line in file:
                if (line.startswith(';') == False) and (line.startswith('\n') == False):
                    self.negatives.add(line.strip())


    def analyze(self, text):
        user_data = set([])
        with open(text, "r") as file:
            for line in file:
                if (line.startswith(';') == False) and (line.startswith('\n') == False):
                    words = word_tokenize(line.strip())
                    for i in range(len(words)):
                        user_data.add(words[i].strip())
        
        if self.positives.intersection(user_data) > self.negatives.intersection(user_data):
            return 1
        elif self.negatives.intersection(user_data) > self.positives.intersection(user_data):
            return -1
        else:
            return 0

