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
from twitter_api.serializers.serializer import FollowersSerializer ,TweetsSerializer
from twitter_api.models import Tweets, UserFollowers

# Create your views here.

class Follow(APIView):

    def post(self,request:Request):
        
        user_id = request.user.id
        payload:Dict = request.data.copy()


        followee_user_id = payload.get('follow',"")

        payload['followee_user'] = payload.pop("follow")[0]
        payload['follower_user'] = user_id

        followee_user = get_object_or_404(User,pk=followee_user_id)
        
        already_follower = UserFollowers.objects.filter(followee_user=payload["followee_user"],follower_user=payload["follower_user"])
        if len(already_follower) > 0:
            return Response("Already followed", status=status.HTTP_409_CONFLICT)
        if followee_user == request.user:
            return Response(data="Cannot follow yourself",status=status.HTTP_409_CONFLICT)
        print(payload)
        
        if followee_user_id == "":
            return Response(data="None to follow",status=status.HTTP_204_NO_CONTENT)

        else:
            serialized_pl = FollowersSerializer(data=payload)
            if serialized_pl.is_valid():
                print("!!!!!!")
                serialized_pl.save()
                return Response(data="Followed"+str(serialized_pl.data),status=status.HTTP_201_CREATED)
            else:
                return Response(data=serialized_pl.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Followers(APIView):
    
    def get(self,request:Request):

        user_id = request.user.id
        my_followers = UserFollowers.objects.filter(followee_user=user_id)
        my_followers_data = FollowersSerializer(my_followers,many=True)
        print(my_followers_data)

        return Response(data=my_followers_data.data,status=status.HTTP_200_OK)

class Followees(APIView):
    
    def get(self,request:Request):

        user_id = request.user.id
        my_followees = UserFollowers.objects.filter(follower_user=user_id)
        my_followees_data = FollowersSerializer(my_followees,many=True)
        print(my_followees)
        return Response(data=my_followees_data.data,status=status.HTTP_200_OK)
