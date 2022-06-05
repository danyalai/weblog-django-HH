from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list_views, name='posts_list'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('form', views.post_form, name='post_form'),
    path('<int:pk>/update/', views.post_update_view, name='post_update'),
    path('<int:pk>/delete/', views.post_delete_view, name='post_delete'),
]
