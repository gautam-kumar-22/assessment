from django.contrib import admin
from django.urls import path
from questions import views
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('result', views.result, name="result"),
]
