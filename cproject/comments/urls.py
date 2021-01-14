from django.urls import path

from . import views


app_name = "comments"


urlpatterns = [
    path("post-comments/", views.base_view, name="base_view"),
    path("create-comment", views.create_comment, name="comment_create"),
    path("create-child-comment", views.comment_child_create, name="comment_child_create")
]
