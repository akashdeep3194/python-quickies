"""twitter_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitter_api.views.Follow_view import Follow, Followees,Followers
from twitter_api.views.Timeline_view import MyTimelineTweets
from twitter_api.views.register_view import RegisterView
from twitter_api.views.Tweet_view import MyTweets
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('mytweets/',MyTweets.as_view()),
    path('mytimeline/',MyTimelineTweets.as_view()),
    path('follow/',Follow.as_view()),
    path('myfollowees/',Followees.as_view()),
    path('myfollowers/',Followers.as_view()),
    path('token/',obtain_auth_token)
]
