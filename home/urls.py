from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('productos/', views.listaproductos),
]