from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from skylark.views import add_post, delete_post, edit_post
from skylark.views import dashboard
from skylark.views import settings, settings_blog, contact_settings
from skylark.views import post_list
from skylark.views import tags_post, tag_post
from cheryl.views import index_pages, index_content
from brasil.views import blog_toggle
from cheryl.views import add_page, modify_page, delete_page
from cheryl.views import (add_content, modify_content,
        delete_content, save_inlinedit)

urlpatterns = patterns('',
        url(r'^$', dashboard, name='skylark_index'),
        url(r'^dashboard/$', dashboard, name='skylark_dashboard'),
        url(r'^brasil/add/$', add_post, name='blog_add_post'),
        url(r'^brasil/delete/(\d+)/$', delete_post,
            name='blog_delete_post'),
        url(r'^brasil/list/$', post_list,
            name='blog_add_post'),
        url(r'^brasil/(\d+)/$', edit_post, name='blog_edit'),
        url(r'^brasil/$', add_post, name='brasil_blog_index'),
        url(r'^brasil/tags/$', tags_post, name='tags'),
        url(r'^brasil/tags/(?P<name>[-\w]+)/$', tag_post, name='tag'),
        url(r'^brasil/toggle/(?P<id>\d+)/$', blog_toggle, name="brasil_toggle"),
        # url(r'^cheryl/?P<id>(\d+)/delete/$', delete_post,
        #     name='blog_delete_post'),
        # url(r'^cheryl/?P<id>(\d+)/edit/$', delete_post,
        #     name='blog_edit_post'),
        # # Brasil pages admin urls
        # url(r'^cheryl/$', brasil_index, name='brasil_index'),
        # url(r'^cheryl/edit/$', brasil_edit, name='brasil_edit'),
        url(r'^cheryl/$', index_pages  ,name='cheryl_list'),
        url(r'^cheryl/add/$', add_page, name='cheryl_add_page'),
        url(r'^cheryl/edit/(?P<id>\d+)/$', modify_page , name='cheryl_edit'),
        url(r'^cheryl/delete/(?P<id>\d+)/$', delete_page , name='cheryl_delete'),
        url(r'^cheryl/content/$', index_content  ,name='cheryl_list'),
        url(r'^cheryl/content/add/$', add_content  ,name='cheryl_list'),
        url(r'^cheryl/content/save/$', save_inlinedit, name='inlineedit'),
        url(r'^cheryl/content/delete/(?P<id>\d+)/$', delete_content  ,name='cheryl_list'),
        url(r'^cheryl/content/(?P<id>\d+)/$', modify_content  ,name='cheryl_list'),
        url(r'^oriel/', include('oriel.urls'), ),
        url(r'^settings/$', direct_to_template, {'template':'preferences.html'}, name="index_settings"),
        url(r'^help/$', direct_to_template, {'template':'help.html'}, name="help"),
        url(r'^settings/page/$', settings, name="settings"),
        url(r'^settings/blog/$', settings_blog, name="settings_blog"),
        url(r'^settings/contact/$', contact_settings, name="settings_contact"),
        # (r'^skylark/users/', include('registration.backends.default.urls') ),
        # url(r'^cheryl/?P<id>(\d+)/delete/$', delete_post,
        #     name='brasil_delete_page'),
        # url(r'^cheryl/?P<id>(\d+)/edit/$', delete_post,
        #     name='brasil_edit_page'),
        )
