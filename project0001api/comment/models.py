from django.db import models
from django.conf import settings
from post.models import Post
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey

class AbstractComment(models.Model):
    """model for Comments"""
    text                = models.TextField(max_length=250)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    is_deleted          = models.BooleanField(default=False)
    is_published        = models.BooleanField(default=False)
    in_moderation       = models. BooleanField(default=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        abstract=True

class Comment(AbstractComment, MPTTModel):
    """Model for post comments"""
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post                = models.ForeignKey(
                                            Post,
                                            related_name='comments' ,
                                            on_delete=models.CASCADE
                                            )
    parent              = TreeForeignKey(
                                        'self',
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        blank=True,
                                        related_name='children'
                                        )

    def __str__(self):
        return '{} - {}'.format(self.user, self.post)