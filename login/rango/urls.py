
from django.conf.urls import patterns, url,include
from rango import views




urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about , name='about'),
        url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^reset/$', views.reset, name='reset'),
        url(r'^newstreet/$' , views.newstreet, name = 'newstreet'),
        url(r'^password_change/$', views.Change_Password),

        
        # Map the 'app.hello.reset_confirm' view that wraps around built-in password
        # reset confirmation view, to the password reset confirmation links.
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.reset_confirm, name='reset_confirm'),
        
        # Map the 'app.hello.success' view to the success message page.
        url(r'^success/$', views.success , name='success'),
        #url(r'^update_user/$', views.update_user , name='update_user'),
        #(r'^contact/thankyou/', views.thankyou),
        #(r'^contact/$', views.contactview ),
    
)




     
