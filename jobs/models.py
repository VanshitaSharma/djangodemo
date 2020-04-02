from django.db import models

# Create your models here.
class job(models.Model):
    title=models.CharField(max_length=100)
    descriptions=models.TextField()
    image=models.ImageField(blank=True)
