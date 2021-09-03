#Daniel Koch 9/3/21 ACM Coding Challenge

from textblob import TextBlob

#read file into a single string with newlines removed
file = open("input.txt")

line = file.read().replace("\n", " ")
file.close()
#source: https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-string-in-python

tblob = TextBlob(line)
print(tblob.sentiment)
