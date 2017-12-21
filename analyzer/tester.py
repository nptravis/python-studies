from analyzer import Analyzer

x = Analyzer("positive-words.txt", "negative-words.txt")
print(x.analyze("hello.txt"))