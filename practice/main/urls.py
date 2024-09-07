from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('clients/', views.clients),
    path('moihiki/', views.moihiki),
    path('zapisi/', views.zapisi),
    path('zapisi/zapisi_change/', views.zapisi_change),
    path('moihiki/moihiki_change/', views.moihiki_change),
    path('clients/clients_change/', views.clients_change)
]
