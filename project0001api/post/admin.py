from django.contrib import admin
from post.models import Post,Comment
from user.models import Badge
from mptt.admin import MPTTModelAdmin

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    """Post administration"""
    list_display = ('user', 'created_at', 'view_count','is_published', 'in_moderation','id')
    #actions = ('publish', 'unpublish')
    mptt_level_intent = 15



@admin.register(Comment)
class AdminPostComment(MPTTModelAdmin, admin.ModelAdmin):
    """Post comments administrations"""
    list_display = ('user', 'post','created_at', 'updated_at','is_published','id')
    #actions = ('publish', 'unpublish')
    mptt_level_intent = 15

@admin.register(Badge)
class AdminBadge(admin.ModelAdmin):
    """Badges administrations"""
    list_display = ('badge_name','badge_image')
    #actions = ('publish', 'unpublish')