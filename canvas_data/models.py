from django.db import models
from django.contrib.auth.models import User


class CanvasData(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='json_files/')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title