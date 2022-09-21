from django.urls import path

from . import views

urlpatterns = [
    path('hello/', views.index, name='index'),
    path('', views.get_players, name='get_players'),
]