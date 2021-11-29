from django.db import models
from django.db.models.deletion import CASCADE,DO_NOTHING,RESTRICT,PROTECT
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Tweets(models.Model):

    date_created = models.DateTimeField(default=now, verbose_name="Created on")
    tweet_data = models.TextField(verbose_name='tweet message')
    user = models.ForeignKey(User,on_delete=DO_NOTHING)

class UserFollowers(models.Model):

    follower_user = models.ForeignKey(User,on_delete=CASCADE,related_name="follower")
    followee_user = models.ForeignKey(User,on_delete=CASCADE,related_name="followee")
