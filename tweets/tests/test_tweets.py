from django.test import TestCase
from users.factories import UsersFactory
from tweets.factories import TweetsFactory
from tweets.models import Tweets


class TestTweetModel(TestCase):
    def setUp(self):
        self.user = UsersFactory(username="joao")
        self.other_user = UsersFactory(username="maria")
        self.tweet = TweetsFactory(user=self.user, content="Primeiro tweet!")

    def test_tweet_creation(self):
        self.assertEqual(self.tweet.user, self.user)
        self.assertEqual(self.tweet.content, "Primeiro tweet!")
        self.assertEqual(self.tweet.likes.count(), 0)

    def test_like_tweet(self):
        self.tweet.likes.add(self.other_user)
        self.assertIn(self.other_user, self.tweet.likes.all())
        self.assertEqual(self.tweet.likes.count(), 1)

    def test_unlike_tweet(self):
        self.tweet.likes.add(self.other_user)
        self.tweet.likes.remove(self.other_user)
        self.assertNotIn(self.other_user, self.tweet.likes.all())
        self.assertEqual(self.tweet.likes.count(), 0)