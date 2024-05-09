from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_ranks, name = 'index'),
    path('api/<str:usuario>/<str:tag>/', views.get_rank, name='index'),
    path('api/all_ranks/', views.get_all_ranks, name='get_all_ranks'),
]