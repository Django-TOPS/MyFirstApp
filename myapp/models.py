from django.db import models

# Create your models here.

class Student(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    sub=models.CharField(max_length=20)
    mobile=models.CharField(max_length=12)

    def __str__(self):
        return self.fullname

class signup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.fname

class mypost(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    category=models.CharField(max_length=50)
    myfile=models.FileField(upload_to='upload')
    comment=models.TextField()

    def __str__(self):
        return self.fname


