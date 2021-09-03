# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!





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