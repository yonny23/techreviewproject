from django.urls import path
from . import views 

#this is a comment
urlpatterns=[
    path('', views.index, name='index'), 


]

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getevents/', views.getevents, name='events'),
    path('eventdetails/<int:id>', views.eventdetails, name='eventdetails'),
    path('newResource/', views.newResource, name='newresource'),
    path('newGreet/', views.newGreet, name='newgreet'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    
]
