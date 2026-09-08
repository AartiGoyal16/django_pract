from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)   
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    # image=models.ImageField()
    file=models.FileField()
    tution_paid=models.BooleanField(default=False)
    
    # id field is auto generated and added by django automatically
    # id=models.AutoField()