from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=50)
    

    

class Familiar1(models.Model):
   
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=50)
    
      

class Familiar2(models.Model):
   
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    profesion=models.CharField(max_length=50)
   
    