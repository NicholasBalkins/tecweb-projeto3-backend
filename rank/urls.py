from django.urls import path
from . import views

urlpatterns = [
    path("api/login/", views.api_get_token, name='index'),
    path("api/cadastro/", views.api_user, name='cadastro'),
    path('api/<str:usuario>/<str:tag>/', views.get_rank, name='index'),
    path('api/all_ranks/', views.get_all_ranks, name='get_all_ranks'),
    path('api/token/', views.api_get_token),
    path('api/users/', views.api_user),
    path("api/historico/<str:usuario>/<str:tag>/", views.historico, name='historico'),
]