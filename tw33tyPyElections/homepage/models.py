from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Tweet(models.Model):
    tweet_text = models.CharField(max_length=280)
    date = models.DateTimeField('date')
    candidate = models.CharField(max_length=100)
    sentiment = models.DecimalField(decimal_places=2,max_digits=5)
    when_searched_for = models.CharField(max_length=100)
    ratio = models.DecimalField(decimal_places=2,max_digits=5)
    likes = models.IntegerField()
    retweets = models.IntegerField()
    replies = models.IntegerField()

    class Meta:
        db_table = 'JanFeb'

    def __str__(self):
        return self.tweet_text
