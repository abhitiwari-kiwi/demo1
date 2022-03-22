from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('home', views.Home.as_view(), name='home'),
    path('add', views.add, name='add'),
    path('edit<str:pk>', views.edit, name='edit'),
    path('delete<str:pk>', views.delete, name='delete'),
    # path('edit', views.edit, name='edit'),
    # path('delete', views.delete, name='delete'),
]