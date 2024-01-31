# Store all urls for the api app
from django.urls import include, path
from .views import RoomView

urlpatterns = [path("home", RoomView.as_view())]
