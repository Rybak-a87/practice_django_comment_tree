from django.shortcuts import render

from .models import Post


def base_view(request):
    comments = Post.objects.first().comments.all()    # вызов коментариев поста
    return render(request, "base/base.html", {"comments": comments})
