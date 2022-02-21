# SGE-Twitter-Dashboard
In this project a sentiment analysis was implemented on tweets for the Bundesliga club Eintracht Frankfurt. It could be seen that the number of tweets peaked during the time of the football matches on Saturday. Eintracht Frankfurt lost both games. That could be the reason for the bigger number of negative tweets compared to the positive ones. Because looking at the other time there seems to be more positive than negative tweets.

## Problem statement / Problem understanding
Within this project a sentiment analysis for tweets on Twitter related to Eintracht Frankfurt is executed in order to identify the sentiment the tweets. This sentiment analysis can help in understanding the feeling of the people about different topics and the current mood related to Eintracht Frankfurt.

## Data Collection & Understanding
The data was collected using Twitter's API via a developer account. The data was scraped using Tweepy for the buzzword / term "SGE". The data was scraped on different days in order to get a higher number of tweets and joined together.

For the moment we have scraped 7362 different tweets in German.

![image](https://user-images.githubusercontent.com/66475927/155017582-bfcd8abb-0bfc-4f57-8d23-dc7a924a9349.png)

We have information regarding the time tweet was posted, content of the tweet, the user which posted the tweet and the location.

## Data Preparation
The data was prepared by extracting first the day of the week, the hour and the minute from the timestamp when the tweet was posted. After that the tweet text was cleaned by removing @, #, links and usernames. Because most of the good Natural Language Processing libraries are in English language the tweets were afterwards translated to English using GoogleTranslator from deep_translator. The last preprocessing step was the removal of the stopwords.

## Model Building
After the data was prepared the analysis was executed. At first the polarity scores for each tweet are computed. Afterwards the compound score was determined and the tweets were categorized in tweets with positive, neutral and negative sentiment depending on their compound score. After this a word cloud was created to get an impression about the words that are mentioned most frequently. Often mentioned words are "SGE", "Eintracht", "Eintracht Frankfurt", "game" and "good" besides others. The next step was to further explore the data in order to get the data ready for the deployment in a plotly dashboard and to extract the most important information. There was also a topic modeling analysis performed but the outcome did not make that much sense. That is the reason why the focus in this project lies on the sentiment analysis.

## Deployment
The sentiment analysis was deployed via Heroku as a plotly Dashboard. In the dashboard the sum of tweets per sentiment for each hour over the whole observed timeline is visible. Moreover, one can also see the total number of tweets per sentiment, the sum of tweets per day and sentiment and the tweets per hour of a day. The dashboard is accessible via: https://sge-twitter-dashboard.herokuapp.com/
