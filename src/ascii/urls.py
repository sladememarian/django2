from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld', views.helloworld),
    path('helloworld/<str:param>', views.helloworld),
]
