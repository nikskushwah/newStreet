import allauth
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newsstreet1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #All Auth URLS
    url(r'^accounts/', include('allauth.urls')),
 
    #Admin Urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
