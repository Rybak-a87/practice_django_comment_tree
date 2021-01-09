from django.urls import path

from . import views


app_name = "comments"


urlpatterns = [
    path("post-comments/", views.base_view, name="base_view"),
]
