from django.db import models


class Badge(models.Model):
    """User achievements in images form"""
    badge_name = models.CharField(max_length=20)  # text representation
    badge_image = models.ImageField(upload_to="badges/", verbose_name='Badge')  # image representation

    def __str__(self):
        return self.badge_name
