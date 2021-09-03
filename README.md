## Daniel Koch - ACM CODING CHALLENGE SENTIMENT ANALYSIS - README


My first step was to google sentiment analysis python and find a library for it. There were multiple results so I found an article comparing the pros and cons of several. https://www.iflexion.com/blog/sentiment-analysis-python
I decided to go with TextBlob because it was said to be simple to use.
I then refreshed myself on how to read a text file in python. https://www.kite.com/python/answers/how-to-read-a-text-file-into-a-string-in-python
Finally, I followed their quickstart tuorial to setup sentiment analysis. https://textblob.readthedocs.io/en/dev/quickstart.html

I recieved a seniment score/polarity of about .2135
This score is within a range of [-1.0, 1.0] meaning the sentiment of the text was found to be positive. 
This fits with what I expected as the majority of the text seemed to be positive descriptions of people.

My solution also produced a subjectivity score of about .5954 which of the range [0.0, 1;0] where 0 is very objective and 1 is very subjective.
Meaning the text was determined to be relatively subjective, which lines up with what I'd expect from reading it.


## END README
