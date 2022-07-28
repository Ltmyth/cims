from django.urls import path
from . import views

# Users urls defined here
urlpatterns = [
    path('', views.index, name='index')
]