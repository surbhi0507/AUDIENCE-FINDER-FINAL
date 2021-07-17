from django.db import models



# Create your models here.
class form(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField()
    contact= models.CharField(max_length=10)
    message= models.TextField()