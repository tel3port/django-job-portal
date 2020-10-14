from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import JobListing
from django.utils.feedgenerator import Atom1Feed


class LatestPostsFeed(Feed):
    title = "JOB LISTING SITE"
    link = ""
    description = "NEW JOB LISTINGS."

    def items(self):
        return JobListing.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.description, 300)


class AtomSiteNewsFeed(LatestPostsFeed):
    feed_type = Atom1Feed
    subtitle = LatestPostsFeed.description
