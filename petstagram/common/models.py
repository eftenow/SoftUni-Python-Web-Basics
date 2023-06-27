from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import Photo

UserModel = get_user_model()


class PhotoComment(models.Model):
    comment_text = models.CharField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    to_user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_time_of_publication']


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='likes')
    to_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='likes')
