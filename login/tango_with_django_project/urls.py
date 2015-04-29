from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from rango import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/password_change/$', 
        'django.contrib.auth.views.password_change', 
        {'post_change_redirect' : '/accounts/password_change/done/'}, 
        name="password_change"), 
    (r'^accounts/password_change/done/$', 
        'django.contrib.auth.views.password_change_done'),
    url(r'^update_user/$', views.update_user , name='update_user'),
    
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
