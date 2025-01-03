from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True) 
    name         = models.CharField(max_length=122)
    description  = models.CharField(max_length=122)
    date         = models.DateField()

