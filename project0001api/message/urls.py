from django.urls import path

from .views import MessageView


app_name = "message"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('message/', MessageView.as_view()),
]