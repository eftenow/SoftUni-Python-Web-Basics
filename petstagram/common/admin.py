from django.contrib import admin

from petstagram.common.models import PhotoComment, PhotoLike


@admin.register(PhotoComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'date_time_of_publication')


