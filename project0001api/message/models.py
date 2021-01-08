from django.db import models
from django.conf import settings

class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    flag = models.BooleanField(default=True,blank=True)
    likes = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return self.message, self.author

class Reply(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    replypost = models.CharField(max_length=240)
    post = models.ForeignKey(Message, verbose_name='対象Post', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name='対象', null=True, blank=True, on_delete=models.CASCADE)
    likes = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.replypost[:10]