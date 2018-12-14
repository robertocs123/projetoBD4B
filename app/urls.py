from django.urls import path , include
from . import views


urlpatterns = [
    path('inicio', views.inicio , name = 'inicio')
]