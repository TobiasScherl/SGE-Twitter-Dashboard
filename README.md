# SGE-Twitter-Dashboard

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
After the data was prepared the analysis was executed. At first the polarity scores for each tweet are computed. Afterwards the compound score was determined and the tweets were categorized in tweets with positive, neutral and negative sentiment depending on their compound score. After this a word cloud was created to get an impression about the words that are mentioned most frequently. Often mentioned words are "SGE", "Eintracht", "Eintracht Frankfurt", "game" and "good" besides others. The next step was to further explore the data in order to get the data ready for the deployment in a plotly dashboard and to extract the most important information.

## Deployment
