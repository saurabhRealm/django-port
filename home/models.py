from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True) 
    name         = models.CharField(max_length=122)
    description  = models.CharField(max_length=122)
    date         = models.DateField()

class Home(models.Model):
    id = models.AutoField(primary_key=True) 
    title         = models.CharField(max_length=122, null=True, blank=True)
    title2         = models.CharField(max_length=122, null=True, blank=True)
    title3         = models.CharField(max_length=122, null=True, blank=True)
    title4         = models.CharField(max_length=122, null=True, blank=True)
    description  = models.CharField(max_length=122, null=True, blank=True)
    description2  = models.CharField(max_length=122, null=True, blank=True)
    date         = models.DateField(null=True, blank=True)
    image        = models.ImageField(upload_to='images/', null=True, blank=True)
    url          = models.URLField(max_length=200, null=True, blank=True)
    slug         = models.SlugField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.title