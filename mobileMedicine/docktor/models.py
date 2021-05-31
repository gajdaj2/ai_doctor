from django.db import models


# Create your models here.


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    specialization = models.ForeignKey('Specialization', on_delete=models.PROTECT)

    def __str__(self):
        return "{} {} {}".format(self.specialization,self.first_name,self.last_name)


class Specialization(models.Model):
    name = models.CharField(max_length=255)
