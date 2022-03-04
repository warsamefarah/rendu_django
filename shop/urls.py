from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:name>/detail/', views.detail, name='detail'),
    path('<str:name>/remove/', views.remove, name='remove'),
]
