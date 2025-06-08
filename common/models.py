from django.db import models

from photos.models import Photo


# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=250)
    date_of_publication = models.DateField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='likes')



