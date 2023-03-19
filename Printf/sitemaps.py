from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Snippet
class StaticViewSitemap(Sitemap):
    def items(self):
        return [{'name': 'home'}]

    def location(self, item):
        return reverse(item['name'])
class SnippetSitemap(Sitemap):
    def items(self):
        return Snippet.objects.all()
    def exclude(self, obj):
        # exclude the t1ss URL
        return obj.slug == 't1ss'
