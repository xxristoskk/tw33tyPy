import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import pymongo
import os
# from homepage import config

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('bar', external_stylesheets=external_stylesheets)

##### Prepare the database
mongo_pw = os.environ['mongo_pw']

## intialize mongodb
client = pymongo.MongoClient(f"mongodb+srv://xtoast:{mongo_pw}@twts0-5a5vv.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.twts0
coll = db['JanFeb']

### Grouping the candidates and summing up the engagements for each tweet
likes = coll.aggregate([{'$group':{'_id':'$candidate','sumLikes':{'$sum':'$likes'}}},{'$sort':{'sumLikes':1}}])
replies = coll.aggregate([{'$group':{'_id':'$candidate','sumReplies':{'$sum':'$replies'}}},{'$sort':{'sumReplies':1}}])
retweets = coll.aggregate([{'$group':{'_id':'$candidate','sumRetweets':{'$sum':'$retweets'}}},{'$sort':{'sumRetweets':1}}])

sumLikes = [x for x in likes]
sumReplies = [x for x in replies]
sumRetweets = [x for x in retweets]

data = [
    {'x': ['Joey', 'Lizzy', 'Bernie'], 'y': [sumLikes[1]['sumLikes'],sumLikes[0]['sumLikes'],sumLikes[2]['sumLikes']],
    'type': 'bar', 'name': 'likes','marker': dict(color='lightsteelblue')},
    {'x': ['Joey', 'Lizzy', 'Bernie'], 'y': [sumReplies[1]['sumReplies'],sumReplies[0]['sumReplies'],sumReplies[2]['sumReplies']],
     'type': 'bar', 'name': 'replies', 'marker': dict(color='lightslategray')},
    {'x': ['Joey', 'Lizzy', 'Bernie'], 'y': [sumRetweets[1]['sumRetweets'],sumRetweets[0]['sumRetweets'],sumRetweets[2]['sumRetweets']],
     'type': 'bar', 'name': 'retweets', 'marker': dict(color='teal')},
]

app.layout = html.Div([
    dcc.Graph(
        id='bar-graph',
        figure={
            'data': data,
            'layout': {
                'title': "Which candidates' name gets the most engagements?"
            }
        }
    ),
])
