from django.contrib import sitemaps
from django.urls import reverse


class PageSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['IndexView', 'AboutView', 'BlogView', 'ContactView']

    def location(self, item):
        return reverse(item)
