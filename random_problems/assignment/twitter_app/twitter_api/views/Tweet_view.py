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
from twitter_api.models import Tweets

# Create your views here.

class MyTweets(APIView):

    def get(self,request:Request):

        user_id = request.user.id
        my_tweets = Tweets.objects.filter(user=user_id)
        my_tweets_data = TweetsSerializer(my_tweets,many=True)
        print(my_tweets)
        return Response(data=my_tweets_data.data,status=status.HTTP_200_OK)

    def post(self,request:Request):
        
        user_id = request.user.id
        payload:Dict = request.data.copy()

        
        tweet_data = payload.get('message',"")
        
        payload['user'] = user_id
        payload['tweet_data'] = payload.pop('message')

        print(payload)
        if tweet_data == "":
            return Response(data="Nothing to tweet",status=status.HTTP_204_NO_CONTENT)

        else:
            serialized_pl = TweetsSerializer(data=payload)
            if serialized_pl.is_valid():
                serialized_pl.save()
                return Response(data="Tweeted"+str(serialized_pl.data),status=status.HTTP_201_CREATED)
            else:
                return Response(serialized_pl.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)