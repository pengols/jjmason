from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
]
