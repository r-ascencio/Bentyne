from django.conf.urls import patterns, include, url
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
# Uncomment the next two lines to enable the admin:
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from skylark.models import Settings
from skylark.models import SettingsBlog as blog_conf
from skylark.models import ContactSettings as contact_conf

from skylark.views import success_contact, contact_send

try:
    blog_settings = blog_conf.objects.get(id=1)
    blog_url = blog_settings.blog_url
    contact_settings = contact_conf.objects.get(id=1)
    contact_url = contact_settings.url
    contact_succes = contact_settings.succes_url
except ObjectDoesNotExist:
    blog_url = 'blog/'
    contact_url = 'contact/'
    contact_succes = 'contact/succes/'


urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'bentyne.views.home', name='home'),
        # url(r'^bentyne/', include('bentyne.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        url(r'^comments/', include('django.contrib.comments.urls')),
        url(r'^content/(?P<title>\w+)', 'cheryl.views.see_content',
            name="see_content"),
        )

urlpatterns += patterns('',
        url(r'^skylark/', include('skylark.urls')),
        (r'^auth/', include('userena.urls')),
        (r'^search/', include('haystack.urls')),
        )

urlpatterns += patterns('',
        url(r'^%s' % contact_url, contact_send),
        url(r'^%s' % contact_succes, success_contact),
        url(r'^%s' % blog_url, include('brasil.urls') ),
        url(r'^(?P<page_url>[\w\d_/-]+)/$', 'cheryl.views.page', name='page_view'),
        url(r'^$', 'cheryl.views.index', name='index_page')
        )


urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        )

#BlogURLChangued

#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued

#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued

#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued

#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued
#BlogURLChangued