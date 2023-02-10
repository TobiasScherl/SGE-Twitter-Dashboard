#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import necessary libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Specify external stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# In[15]:


# Read in preprocessed data from csv files to pandas dataframes
df = pd.read_csv('df_sentiment_SGE.csv')
df_day = pd.read_csv('df_day_SGE.csv')
df_hour = pd.read_csv('df_hour_SGE.csv')
df_totalTweets = pd.read_csv('df_totalTweets_SGE.csv')
df_topUser = pd.read_csv('df_topUser.csv')
df_subjectivity = pd.read_csv('df_subjectivity.csv')


# In[16]:


# Specify plotly dahsboards
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Specify the figures
fig1 = px.line(df, x="datetime", y=["pos","neg","neu"])
fig2 = px.pie(df_totalTweets, values='value', names='com_score')
fig3 = px.bar(df_day, x="day", y=["pos","neg","neu"])
fig4 = px.bar(df_hour, x="Hour", y=["pos","neg","neu"])
fig5 = px.bar(df_topUser, x="User", y="value")
fig6 = px.line(df_subjectivity, x="datetime", y=["Objective","Subjective"])
#fig5 = px.pie(df_topUser, names="User", values="value")



app.layout = html.Div(children=[
    html.Div([
        html.H1(children='Sentiment Analysis of Eintracht Frankfurt Tweets'),

        html.Div(children='''
            Hourly Number of SGE related Tweets grouped by Sentiment
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
    ])
    ,
    html.Div([
        html.H1(children='Total number of SGE Tweets per Sentiment'),

        html.Div(children='''
            Sentiments sorted according to their compound scores
        '''),

        dcc.Graph(
            id='graph2',
            figure=fig2
        ),  
    ])
    ,
    html.Div([
        html.H1(children='Sum of SGE Tweets per Day and Sentiment'),

        html.Div(children='''
            Tweets summed per day and sentiment
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig3
        ),  
    ])
    ,
    html.Div([
        html.H1(children='Sum of SGE Tweets per Hour of a Day and Sentiment'),

        html.Div(children='''
            Tweets summed per hour of a day by sentiment
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),  
    ]),
    html.Div([
        html.H1(children='Twitter SGE Top Users'),

        html.Div(children='''
            Number of Tweets for Users with more than 25 Tweets sorted from top to bottom
        '''),

        dcc.Graph(
            id='graph5',
            figure=fig5
        ),  
    ]),
    html.Div([
        html.H1(children='Subjectivity of Tweets count by datetime'),

        html.Div(children='''
            Number of Tweets grouped by their subjectivity and hour
        '''),

        dcc.Graph(
            id='graph6',
            figure=fig6
        ),  
    ]),
])


# In[17]:


if __name__ == '__main__':
    app.run_server()


# In[ ]:





# In[ ]:




