from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm

from docktor.models import Doctor


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    customer_id = models.CharField(max_length=11)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    date = models.DateTimeField()
    room = models.CharField(max_length=255)


class CustomerView(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'city', 'zip_code', 'mobile', 'email']


class HeartAttack(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trtbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalachh = models.IntegerField()
    exng = models.IntegerField()
    oldpeak = models.IntegerField()
    slp = models.IntegerField()
    caa = models.IntegerField()
    thall = models.IntegerField()


class HeartAttackView(ModelForm):
    class Meta:
        model = HeartAttack
        fields = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa',
                  'thall']


class Diabetes(models.Model):
    pregnancies = models.IntegerField(max_length=2)
    glucose = models.FloatField()
    diastolic = models.FloatField()
    triceps = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    dpf = models.FloatField()
    age = models.IntegerField(default=0)
    diabetes = models.FloatField()


class DiabetesView(ModelForm):
    class Meta:
        model = Diabetes
        fields = ['pregnancies', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi', 'dpf', 'age']
