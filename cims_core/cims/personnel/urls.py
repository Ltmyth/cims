from django.urls import path
from . import views

# URLS for personnel written here
urlpatterns = [
    path('', views.index, name="index"),
]