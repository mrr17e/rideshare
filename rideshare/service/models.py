from django.db import models

class rideshare(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=30, null=False)
    dl = models.CharField(max_length=40, null=False)
    vt = models.CharField(max_length=20)
    vlno = models.CharField(max_length=40, null=False)
    phone = models.IntegerField(null=False)
    stavl = models.IntegerField()
    startl = models.CharField(max_length=50)
    lastl = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    dlphoto = models.ImageField(upload_to='media/')

