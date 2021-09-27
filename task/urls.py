from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/quotes', views.ConversionList.as_view()),
    #path('api/v1/quotes', views.ConversionList.as_view()),
]
