from django.urls import path
from .views import ShortenURLView, redirect_view, home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("shorten/", ShortenURLView.as_view()),
    path("<str:code>/", redirect_view),
]
