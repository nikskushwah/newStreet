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
    url(r'^password_change/$', 'rango.views.Change_Password'),
   
    
    url(r'^update_user/$', views.update_user , name='update_user'),
    #(r'^accounts/', include('registration.backends.simple.urls')),
    #(r'^changepassword/$', views.Change_Password),

    
    (r'^contact/thankyou/', 'rango.views.thankyou'),
    (r'^rango/contact/', 'rango.views.contactview'),
    #(r'^password_change/$', views.Change_Password),
    
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
