from rest_framework import serializers
from follows.models import Follows
from users.models import Users

class FollowsSerializer(serializers.ModelSerializer):
    follower_username = serializers.CharField(source='follower.username', read_only=True)
    following_username = serializers.CharField(source='following.username', read_only=True)

    class Meta:
        model = Follows
        fields = ['id', 'follower', 'following', 'follower_username', 'following_username']