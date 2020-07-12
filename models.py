from django.db import models

class patient(models.Model):
    password=models.CharField(max_length=20,primary_key=True);
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20);
    bloodgroup = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    chance=models.CharField(max_length=20)
    sugg=models.CharField(max_length=20)




class feedbackform(models.Model):
    feed=models.CharField(max_length=100,primary_key=True);

