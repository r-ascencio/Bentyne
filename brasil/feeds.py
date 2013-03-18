from django.contrib.syndication.views import Feed
from django.core.exceptions import ObjectDoesNotExist
from brasil.models import Post
from skylark.models import Settings as site_conf
from skylark.models import SettingsBlog as blog_conf

try:
    site_settings = blog_conf.objects.get(id=1)
    alpha_settings = site_conf.objects.get(id=1)
    title = site_settings.blog_title
    domain = alpha_settings.site_domain
    blog_url = site_settings.blog_url
    blog_description = site_settings.blog_description
except ObjectDoesNotExist:
    title = 'blog'
    domain = 'example.com'
    blog_url = '/blog/'
    blog_description = 'Rasta Science'


class PostsFeed(Feed):
    title = "%s news" % title
    link = "%s/%s" % (domain, blog_url)
    description = "%s" % blog_description

    def items(self):
        return Post.objects.order_by('-id')[:5]

    def item_title(self, item):
        return item.title

    def item_body(self, item):
        return item.body
