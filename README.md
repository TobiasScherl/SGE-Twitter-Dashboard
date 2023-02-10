# SGE-Twitter-Dashboard
In this project a sentiment analysis was implemented on tweets for the Bundesliga club Eintracht Frankfurt. It could be seen that the number of tweets peaked during the time of a football match on Wednesday. Eintracht Frankfurt won this game. That could be the reason for the bigger number of positive tweets compared to neutral or negative ones. Because looking at the other periods of time there seems to be tendency of more neutral tweets and also a smaller ratio between positive and negative tweets. It is also visible the subjectivity of the tweets and who the top users (measured in the number of tweets) are. Not surprisingly the account of the club is one of the top users with most of the tweets.

## Problem statement / Problem understanding
Within this project a sentiment analysis for tweets on Twitter related to Eintracht Frankfurt is executed in order to identify the sentiment of the tweets. This sentiment analysis can help in understanding the current mood related to Eintracht Frankfurt.

## Data Collection & Understanding
The data was collected using Twitter's API via a developer account. The data was scraped using Tweepy for the buzzword / term "SGE". The data was scraped for a certain period of time. 

![image](https://user-images.githubusercontent.com/66475927/218162508-5701fc2d-eb68-4d1a-bbfb-559c7dd82b6d.png)

In the end the data was taken for the period of the 6th until the 8th of February. The dataframe contains therefore 2024 tweets in total (of actually 14549 collected tweets). All tweets are in German language.

We have information regarding the time the tweet was posted, content of the tweet, the user which posted the tweet and the location.

## Data Preparation
The data was prepared by extracting first the day of the week, the hour and the minute from the timestamp when the tweet was posted. After that the tweet text was cleaned by removing @, #, links and usernames. Because most of the Natural Language Processing libraries are in English language the tweets were afterwards translated to English using GoogleTranslator from deep_translator. The last preprocessing step was the removal of the stopwords.

## Model Building
After the data was prepared the analysis was executed. At first the polarity scores for each tweet are computed. Afterwards the compound score was determined and the tweets were categorized in tweets with positive, neutral and negative sentiment depending on their compound score. After this a word cloud was created to get an impression about the words that are mentioned most frequently. Often mentioned words are "SGE", "Eintracht", "DFB", "Cup" and "SBU" besides others.

![image](https://user-images.githubusercontent.com/66475927/218163506-609e5b1d-61af-4fe0-8026-f838c4a8f731.png)

The next step was to further explore the data in order to get the data ready for the deployment in a plotly dashboard and to extract the most important features out of the data.

## Deployment
The dashboard was built with plotly and the information extracted is visualized there. In the dashboard the sum of tweets per sentiment for each hour over the whole observed timeline is visible. Moreover, one can also see the total number of tweets per sentiment, the sum of tweets per day and sentiment and the tweets per hour of a day. Furthermore, subjectivity and top users are visible.
