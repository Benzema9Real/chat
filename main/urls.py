from . import views
from django.urls import path

urlpatterns = [path('', views.index),
               path('chat/', views.my_view, name="chat"),
               path('entering_messages', views.create, name='entering'),


               ]
