from rest_framework import serializers
from tweets.models import Tweets
from users.models import Users

class TweetsSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Tweets
        fields = ['id', 'user', 'username', 'content', 'created_at', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user in instance.likes.all():
            instance.likes.remove(user)
        else:
            instance.likes.add(user)
        return instance