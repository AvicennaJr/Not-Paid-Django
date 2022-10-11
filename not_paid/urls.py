from django.urls import path
import views

url_pattern = [
    path("", views.index, name=('index')),
]