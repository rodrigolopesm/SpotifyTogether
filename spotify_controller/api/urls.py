# Store all urls for the api app
from django.urls import include, path
from .views import main

urlpatterns = [
    path("home", main),
]
