from django.contrib.sitemaps import Sitemap
from .models import Blog


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
 
    def items(self):
        return Blog.objects.filter(public=True).order_by('-created')
 
    def lastmod(self, obj):
    	return obj.created
