import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import pymongo
import os
# from homepage import config

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('sentiment', external_stylesheets=external_stylesheets)

##### Prepare the database
mongo_pw = os.environ['mongo_pw']

## intialize mongodb
client = pymongo.MongoClient(f"mongodb+srv://xtoast:{mongo_pw}@twts0-5a5vv.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.twts0
coll = db['JanFeb']

### Grouping the candidates and averaging the sentiment of tweets
s = coll.aggregate([{'$group':{'_id':'$candidate','avgSentiment':{'$avg':'$sentiment'}}},{'$sort':{'avgSentiment':1}}])
sentiment = [x['avgSentiment'] for x in s]

data = [
    {'x': ['Joey','Lizzy','Bernie'],
     'y': [sentiment[0], sentiment[1], sentiment[2]],
     'type': 'bar',
     'marker': dict(color=['lightsteelblue','lightslategray','teal']),
     'textposition': 'auto'
     }
]
app.layout = html.Div([
    dcc.Graph(
        id='bar-graph',
        figure={
            'data': data,
            'layout': {
                'title': "What is the average sentiment for tweets associated with each candidate?"
            }
        }
    ),
])
