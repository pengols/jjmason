from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog'),
    path('add/', views.add_post, name='add_post'),
]
