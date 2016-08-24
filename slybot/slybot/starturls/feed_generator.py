from scrapy import Request


class FeedGenerator(object):
    def __init__(self, callback):
        self.callback = callback

    def __call__(self, url):
        return Request(url, callback=self.parse_urls)

    def parse_urls(self, response):
        urls = [url for url in response.text.split('\n') if url]
        for url in urls:
            yield Request(url, callback=self.callback)
