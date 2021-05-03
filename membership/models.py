from django.db import models


# Create your models here.
class Membership(models.Model):
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    gender = models.CharField(max_length=4)
    height = models.CharField(max_length=5)  # 소수점 둘째자리까지
    weight = models.CharField(max_length=5)  # 소수점 둘째자리까지

    class Meta:
        ordering = ['name']
