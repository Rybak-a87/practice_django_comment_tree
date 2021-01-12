from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Название поста")
    text = models.TextField(verbose_name="Текст")
    comments = GenericRelation("comment")    # привязка комментариев (в shell - post.comments.all() - выведет коментарии к посту)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст комментария")
    parent = models.ForeignKey(    # ссылается на другой комментарий
        "self", verbose_name="Родительский комментарий", on_delete=models.CASCADE,
        blank=True, null=True, related_name="comment_children"
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)    # для привязки комментариев к чему угодно
    object_id = models.PositiveIntegerField()

    timestamp = models.DateTimeField(auto_now=True, verbose_name="Дата создания комментария")
    is_child = models.BooleanField(default=False, verbose_name="Дочерний комментарий")
    ''' модно добавить лайки, дизлайки и т.д. '''

    def __str__(self):
        return str(self.id)

    @property
    def get_parent(self):    # id родительского комментария
        if not self.parent:
            return ""
        return self.parent
