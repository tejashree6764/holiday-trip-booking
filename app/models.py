from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=300)

    def __str__(self):
     return self.name

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=50)
    timeStamp=models.DateTimeField(blank=True)     

class Register(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    gender=models.CharField(max_length=20)
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)

    def __str__(self):
     return self.name

    