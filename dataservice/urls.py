from django.contrib import admin
from django.urls import path, include
from dataservice import views

urlpatterns = [
    path("generate-code", views.generate_code, name='generate-code'),
    path("get_code_by_url", views.get_code_by_url, name='get_code_by_url'),
    path("", views.index, name='index'),

]