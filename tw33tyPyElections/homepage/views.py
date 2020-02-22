from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import random as r
import pymongo
import os
# from homepage import config

mongo_pw = os.environ['mongo_pw']

client = pymongo.MongoClient(f"mongodb+srv://xtoast:{mongo_pw}@twts0-5a5vv.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.twts0
coll = db['JanFeb']

def home(request):
    ### Find tweets with a 2:1 reply:like ratio
    bq = coll.find({'ratio':{'$gt':2},'candidate':'sanders'})
    jq = coll.find({'ratio':{'$gt':2},'candidate':'biden'})
    lq = coll.find({'ratio':{'$gt':2},'candidate':'warren'})
    b_list = [t for t in bq if t['likes']>100]
    j_list = [t for t in jq if t['likes']>100]
    l_list = [t for t in lq if t['likes']>100]
    bernie = b_list[r.randint(0,len(b_list))]
    joey = j_list[r.randint(0,len(j_list))]
    lizzy = l_list[r.randint(0,len(l_list))]
    context = {'btweet': bernie['tweet'],
               'jtweet': joey['tweet'],
               'ltweet': lizzy['tweet'],
               'bratio': format(bernie['ratio'],'.2f'),
               'jratio': format(joey['ratio'],'.2f'),
               'lratio': format(lizzy['ratio'],'.2f')}
    return render(request,'homepage/home.html',context)
