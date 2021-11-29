from re import M
from typing import Dict
from django.db.models import manager
from django.http import response
from django.shortcuts import get_list_or_404, render, get_object_or_404
from rest_framework import request
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from twitter_api.serializers.serializer import TweetsSerializer
from twitter_api.models import Tweets, UserFollowers

# Create your views here.

class MyTimelineTweets(APIView):

    def get(self,request:Request):

        user_idx = request.user.id
        print(user_idx)
        myfollowees = UserFollowers.objects.filter(follower_user=user_idx)
        print(myfollowees)
        myfolloweeslist = []
        for ele in myfollowees:
            myfolloweeslist.append(ele.followee_user.id)

        # my_timeline_tweets = Tweets.objects.filter(user_id__in = myfolloweeslist)
        my_timeline_tweets = Tweets.objects.filter(user__followee__follower_user=user_idx).order_by('-date_created')

        my_timeline_tweets_data = TweetsSerializer(my_timeline_tweets,many=True)
        print(my_timeline_tweets)
        return Response(data=my_timeline_tweets_data.data,status=status.HTTP_200_OK)
