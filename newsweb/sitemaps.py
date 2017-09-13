from django.contrib.sitemaps import Sitemap

from homepage.models import News

class TodoSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return News.objects.all()