from django.contrib.sitemaps import Sitemap
from .models import Post
class PostSitemap(Sitemap):
    changefreq='daily'
    priorty=0.9
    def items(self):
        return Post.objects.all()
    def lastmod(self,obj):
        return obj.add_date