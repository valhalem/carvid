from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'article.views.index',),
    url(r'^$', 'index', name='index'),
    # url(r'^carvid/', include('carvid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/$', 'article.views.index'),
    url(r'^article/(?P<article>\d+)/$', 'article.views.article_details'),
    url(r'^tags/', 'article.views.tags'),
    url(r'^tag/(?P<tag>\w+)/$', 'article.views.tags_search'),
)
