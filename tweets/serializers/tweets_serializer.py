from rest_framework import serializers
from tweets.models import Tweets

class TweetsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tweets
        fields = ['id', 'user', 'username', 'content', 'created_at']