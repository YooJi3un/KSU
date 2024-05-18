# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/images/')
    video = models.FileField(upload_to='artworks/videos/', blank=True, null=True)  # 비디오 필드 추가
    section = models.CharField(max_length=100, default='general')

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:20]  # 댓글의 처음 20자를 표시
