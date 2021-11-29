from rest_framework.serializers import ModelSerializer
from twitter_api.models import Tweets, UserFollowers


class TweetsSerializer(ModelSerializer):

    class Meta:
        model = Tweets
        fields = '__all__'

class FollowersSerializer(ModelSerializer):

    class Meta:
        model = UserFollowers
        fields = '__all__'
