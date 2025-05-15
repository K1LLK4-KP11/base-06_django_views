from django.urls import path
from posts import views 

urlpatterns = [
    path('list', views.post_list, name='ptsd list'),
    path('detail', views.post_detail, name='ptsd detail'),
    path('create', views.PostCreateView, name='create ptsd'),
]