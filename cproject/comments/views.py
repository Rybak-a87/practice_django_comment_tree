from django.shortcuts import render

from .models import Post
from .utils import create_comments_tree


def base_view(request):
    comments = Post.objects.first().comments.all()    # вызов комментариев поста
    result = create_comments_tree(comments)
    for res in result:
        print(res)
        print("-----------")
    return render(request, "base/base.html", {"comments": comments})
