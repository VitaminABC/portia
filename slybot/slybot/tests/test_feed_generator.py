import scrapy

from unittest import TestCase

from slybot.starturls import FeedGenerator


class FeedGeneratorTest(TestCase):
    def test_feed_urls(self):
        url = 'http://feed_domain.com'
        callback = lambda x: x
        generator = FeedGenerator(callback)

        feed_urls = generator(url)
        self.assertTrue(isinstance(feed_urls, scrapy.Request))
        self.assertEqual(feed_urls.url, url)
