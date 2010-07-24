from django.contrib.syndication.views import Feed
from home.models import NewsItem
class LatestNewsFeed(Feed):
    title = "Cseismic 2k10 RSS News Feed"
    link = "/feed/rss"
    description = "Updates on events and results on Cseismic 2k10"

    def items(self):
        return NewsItem.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.message

    def item_description(self, item):
        return item.message
        
    def item_link(self, item):
        return self.link
