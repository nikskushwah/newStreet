from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^accounts/', include('newstreet.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
"""url(r'^accounts/password_change/$', 
        'django.contrib.auth.views.password_change', 
        {'post_change_redirect' : '/accounts/password_change/done/'}, 
        name="password_change"), 
    (r'^accounts/password_change/done/$', 
        'django.contrib.auth.views.password_change_done'),
<p>click <a href="/accounts/password_change">change password</a> to edit your password</p>"""