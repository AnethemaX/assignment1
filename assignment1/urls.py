from django.conf.urls import patterns, include, url
from django.contrib import admin
from bookmarks import views

urlpatterns = patterns('',
    url(r'^list/$', views.bookmark_list, name='bookmark_list'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/(?P<bookmark_id>\d+)$', views.bookmark_detail, name='detail'),

)
