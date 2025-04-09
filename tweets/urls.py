from django.urls import path, include
from rest_framework import routers
from tweets.viewsets import TweetViewSet

router = routers.SimpleRouter()
router.register(r'', TweetViewSet, basename="tweets")

urlpatterns = [
    path("", include(router.urls)),
]