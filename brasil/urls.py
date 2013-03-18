from django.conf.urls.defaults import patterns, include, url
# Blog - features
from brasil.views import blog_index, blog_detail
from brasil.feeds import PostsFeed

urlpatterns = patterns('',
        url(r'^$', blog_index, name="brasil_index"),
        url(r'^feed/$', PostsFeed()),
        url(r'^(?P<slug>[-\w]+)/$', blog_detail, name="brasil_detail"),
        )
