from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from jobs.models import JobListing


class StaticViewsJobListingSitemap(Sitemap):
    changefreq = 'always'
    priority = 1.0

    def items(self):
        return JobListing.objects.all()
