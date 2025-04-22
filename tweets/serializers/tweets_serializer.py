from rest_framework import serializers
from tweets.models import Tweets
from tweets.models import Comments

class TweetsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Tweets
        fields = ['id', 'user', 'username', 'content', 'created_at', 'likes_count', 'is_liked']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return obj.likes.filter(id=user.id).exists() if user.is_authenticated else False
    
class CommentsSerializer(serializers.ModelSerializer):
    tweet = serializers.PrimaryKeyRelatedField(queryset=Tweets.objects.all())
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'content', 'tweet', 'user', 'created_at']

