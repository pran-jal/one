from django.db import models


# Create your models here.
class Post(models.Model):
    def __str__(self) -> str:
        return self.title

    title = models.CharField(max_length = 30)
    text = models.TextField()

class student(models.Model):
    def __str__(self) -> str:
        return self.name

    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 50)
    marks = models.IntegerField()