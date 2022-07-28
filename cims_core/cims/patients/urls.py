from django.urls import path
from . import views

#Patient Urls written here
urlpatterns = [
    path('', views.index, name='index'),
]