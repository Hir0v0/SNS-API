from django.db import models
from django.conf import settings
from comment.models import AbstractComment
from mptt.models import MPTTModel,TreeForeignKey

# Create your models here.
class Post(models.Model):
    """Users post model"""
    text                = models.TextField(max_length=250)
    created_at          = models.DateTimeField(auto_now_add=True)
    is_published        = models.BooleanField(default=False)
    is_deleted          = models.BooleanField(default=False)
    in_moderation       = models.BooleanField(default=True)
    view_count          = models.PositiveIntegerField(default=0)
    user                = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'Posted by {self.id}'

    def comments_count(self):
        return self.comments.count()

class Comment(AbstractComment, MPTTModel):
    """Model for post comments"""
    user              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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