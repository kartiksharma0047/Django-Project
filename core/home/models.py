from django.db import models

# Create your models here.
class Student(models.Model):
    # Id is Primary Key
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True)
    image=models.ImageField()
    file=models.FileField()