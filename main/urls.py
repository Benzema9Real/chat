from django.contrib.auth.views import LoginView

from . import views
from django.urls import path

urlpatterns = [path('', views.main,name="main"),
               path('chat/', views.my_view, name="chat"),
               path('registr/', views.registr, name='registr'),
               path('entering_messages', views.create, name='entering'),
path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),


               ]
