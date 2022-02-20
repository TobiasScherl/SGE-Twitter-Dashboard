import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('df_sentiment_SGE.csv')
df_day = pd.read_csv('df_day_SGE.csv')
df_hour = pd.read_csv('df_hour_SGE.csv')
df_totalTweets = pd.read_csv('df_totalTweets_SGE.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

fig1 = px.line(df, x="datetime", y=["pos","neg","neu"], template="plotly_dark")
fig2 = px.bar(df_totalTweets, y='value', x='com_score', template="plotly_dark")#, title='Total number of Tweets per Sentiment')
fig3 = px.bar(df_day, x="day", y=["pos","neg","neu"], template="plotly_dark")
fig4 = px.bar(df_hour, x="Hour", y=["pos","neg","neu"], template="plotly_dark")



app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Sentiment Analysis of Eintracht Frankfurt Tweets'),

        html.Div(children='''
            Hourly Number of SGE related Tweets summed by Sentiment
        '''),

        dcc.Graph(
            id='graph1',
            figure=fig1
        ),  
    ])
    ,
    # New Div for all elements in the new 'row' of the page
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
            Tweets sorted per day and sentiment
        '''),

        dcc.Graph(
            id='graph3',
            figure=fig3
        ),  
    ])
    ,
    html.Div([
        html.H1(children='SGE Tweets per Hour of a Day'),

        html.Div(children='''
            Tweets summed per hour of a day by sentiment
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),  
    ]),
])

                 
if __name__ == '__main__':
    app.run_server()