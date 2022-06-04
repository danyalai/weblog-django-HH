from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list_views, name='posts_list'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('form', views.post_form, name='post_form')
]
