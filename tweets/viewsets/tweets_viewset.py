from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from tweets.models import Tweets
from tweets.serializers import TweetsSerializer
from follows.models import Follows

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweets.objects.all().order_by('-created_at')
    serializer_class = TweetsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def following(self, request):
        following_ids = Follows.objects.filter(
            follower=request.user
        ).values_list("following_id", flat=True)

        tweets = Tweets.objects.filter(user_id__in=following_ids).order_by("-created_at")
        serializer = self.get_serializer(tweets, many=True)
        return Response(serializer.data)