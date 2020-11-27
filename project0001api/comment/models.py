from django.db import models

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