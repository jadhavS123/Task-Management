from django.db import models

# Create your models here.
class Article(models.Model):   # Creating a model
    name = models.CharField(max_length=25)   
    date = models.CharField(max_length=25)   
    clas = models.CharField(max_length=25)   
    


# 3 ways  to perform CRUD

# Admin Panel
# Shell   --- get interactive console
# Django views





