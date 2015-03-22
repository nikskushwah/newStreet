from django.conf.urls import patterns,url
from django.contrib import admin
from login import views
urlpatterns = patterns('',
    url(r'^register/$',views.register,name='register')
)
