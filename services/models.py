from django.db import models


class ServiceData(models.Model):
    head = models.CharField(max_length=50)
    des = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='pic')
