from django.db import models

# Create your models here.
class Content(models.Model):
    title=models.CharField(max_length=25)
    describtion=models.TextField()
