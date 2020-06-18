from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    # content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class us(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class video(models.Model):
    title = models.CharField(max_length=100)
    video_file =models.FileField(upload_to='video_files')
    discription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
