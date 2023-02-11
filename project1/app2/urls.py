from django.urls import path

from.views import UserAPI



urlpatterns = [
    path('register/',UserAPI.as_view())
]