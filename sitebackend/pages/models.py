from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=10)
    url = models.CharField(max_length=500)
    about = models.CharField(max_length=500)
    def __str__(self):
        return f"Project: {self.name}"
        return f"URL: {self.url}"