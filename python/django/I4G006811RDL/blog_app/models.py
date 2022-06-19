from django.db import models

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.CharField(max_length=200)
    Author=models.ForeignKey("Post", on_delete=models.CASCADE)
    Created_date=models.DateTimeField()
    Published_date=models.DateTimeField()

