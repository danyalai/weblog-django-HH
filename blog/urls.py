from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_views, name='posts_list'),
]
