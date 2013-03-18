from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from oriel.views import PictureCreateView, PictureDeleteView
from oriel.views import gallery_list, add_gallery, edit_gallery, view_gallery
from oriel.views import show_gallery
from oriel.views import edit_picture, delete_picture

urlpatterns = patterns('',
    # (r'^new/$', PictureCreateView.as_view(), {}, 'upload-new'),
    url(r'^upload/(?P<slug>[-\w]+)/$', PictureCreateView.as_view(), {}, 'upload-new'),
    url(r'^add/$', add_gallery, name='gallery-new'),
    url(r'^show/(?P<slug>[-\w]+)/$', show_gallery, name='gallery-show'),
    url(r'^$', gallery_list, name='oriel_index'),
    url(r'^(?P<slug>[-\w]+)/$',  view_gallery, name='gallery-edit'),
    (r'^rm/picture/(?P<pk>\d+)/$', login_required(PictureDeleteView.as_view()),
        {}, 'upload-delete'),
    url(r'^picture/(?P<id>\d+)/$', edit_picture, {}, 'picture-edit'),
    url(r'^delete/picture/(?P<id>\d+)/$', delete_picture, {}, 'picture-delete'),
)
