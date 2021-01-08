from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст комментария")
    parent = models.ForeignKey(    # ссылается на другой коментарий
        "self", verbose_name="Родительский коментарий", on_delete=models.CASCADE,
        blank=True, null=True, related_name="comment_children"
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    time_stamp = models.DateTimeField(auto_now=True, verbose_name="Дата создания комментария")
    ''' модно добавить лайки, дизрайки и т.д. '''

    def __str__(self):
        return str(self.id)
