# FinAlyze
Application to track stock sentiment based on news articles. 
Sentiment analysis will be used to determine a personal stocks portfolio.
Data obtained using Polygon API. 

## 

## TODO
### Backend
* Handle the API calls 
* Parse data
* Use machine learning to analyze data

### Frontend (GUI)

### Features
* Analyze growth stocks 
* Apply machine learning/deep learning/ AI algorithms to analyze articles and categorize them by sentiment value
* Updates on owned stocks 
* Tracking stocks 


## Log
2/6/2023
* Restructured files
* Added datehandler.py to handle dates (trading days, timestamps)
* Modify client.py to a class 

2/3/2023
* Decoding and parsing HTTP URL responses

2/2/2023
* Included screener database, currently working on implementing auto calls

12/21/2022
* Researched NLP methods for text sentiment. Will use Aspect-Based Sentiment analysis. 
    * Learning Span-Level Interactions for Aspect Sentiment Triplet Extraction research paper github: https://github.com/chiayewken/Span-ASTE

12/20/2022
* Subscribed to free version of Polygon API.
* Created Polygon API environment variable
* Added function to obtain stock news
* Added function to parse description data and write contents to file.
