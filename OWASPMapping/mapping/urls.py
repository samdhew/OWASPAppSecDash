from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.layout),
    path('list/', views.listAll),
    path('add/', views.add)
]
