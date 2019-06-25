from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.layout),
    path('list/', views.list),
    path('add/', views.add)
]
