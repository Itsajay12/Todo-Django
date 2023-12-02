from django.urls import path
from .views import*
urlpatterns = [

    path('',index,name='index'),
    path('register/',register_user,name="register"),
    path('login/',login_user,name="login"),
    path('logout/',logout_user,name="logout"),
    path('completed/<int:id>',completed,name="completed"),
     path('deleted/<int:id>',deleted,name="deleted"),
      path('important/<int:id>',important,name="important"),
      path('statusload/<str:status>',satus_load,name='statusload'),
      path('deletetask/<int:id>',delete_task,name="deletetask"),
      path('today/',today,name="today"),
]