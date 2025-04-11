from rest_framework import serializers
from users.models import Users
from follows.models import Follows

class UsersSerializer(serializers.ModelSerializer):
    is_following = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'is_following']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Users(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_is_following(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Follows.objects.filter(follower=request.user, following=obj).exists()
        return False