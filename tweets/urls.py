from django.urls import path, include
from rest_framework import routers
from tweets.viewsets import TweetsViewSet

router = routers.SimpleRouter()
router.register(r'', TweetsViewSet, basename="tweets")

urlpatterns = [
    path("", include(router.urls)),
]