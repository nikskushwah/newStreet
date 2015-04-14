from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
	    url(r'^profile/$', 'newstreet.views.user_profile'),
)