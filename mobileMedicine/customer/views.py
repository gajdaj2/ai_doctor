import time

from asgiref.sync import sync_to_async
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_protect

from customer.analysis.mdoctor import MDoctor
from customer.models import DiabetesView, HeartAttackView, Customer, CustomerView

user = None


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        global user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'customer/landing.html', {'username': user})
        else:
            messages.add_message(request, messages.ERROR, 'Wrong password or user')
    return render(request, 'customer/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username, password, email)
    return render(request, 'customer/register.html')


@login_required
def heart(request):
    heartForm = HeartAttackView()
    return render(request, 'customer/heart.html', {'form': heartForm})


@login_required
def diabetes(request):
    if user is not None:
        diabetesForm = DiabetesView()
        if request.method == 'POST':
            form = DiabetesView(request.POST)
            if form.is_valid():
                pregnancies = form.cleaned_data['pregnancies']
                glucose = form.cleaned_data['glucose']
                diastolic = form.cleaned_data['diastolic']
                triceps = form.cleaned_data['triceps']
                insulin = form.cleaned_data['insulin']
                bmi = form.cleaned_data['bmi']
                dpf = form.cleaned_data['dpf']
                age = form.cleaned_data['age']
                doctor = MDoctor()
                x, y = doctor \
                    .data_analysis('data/diabetes.csv',
                                   [pregnancies, glucose, diastolic, triceps, insulin, bmi, dpf, age])
                return render(request, 'customer/diabetes.html', {'form': diabetesForm, 'pos': x, 'neg': y})
        else:
            return render(request, 'customer/diabetes.html', {'form': diabetesForm})
    else:
        return render(request, "customer/index.html")


def add_customer_information(request):
    global user
    form = CustomerView()
    if user is not None:
        if request.method == 'POST':
            form = CustomerView(request.POST)
            if form.is_valid():
                Customer.objects.create(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],
                                        address=form.cleaned_data['address'], city=form.cleaned_data['city'],
                                        zip_code=form.cleaned_data['zip_code'], mobile=form.cleaned_data['mobile'],
                                        email=form.cleaned_data['email'], user=user)
        else:
            return render(request, 'customer/add_customer_information.html', {'form': form})
    return render(request, 'customer/add_customer_information.html', {'form': form})


@login_required
def landing(request):
    if user is not None:
        if request.method == 'POST':
            return render(request, 'customer/landing.html')
        else:
            return render(request, 'customer/landing.html')
    else:
        return render(request, "customer/index.html")


def logout(request):
    global user
    if user is not None:
        user = None
    return render(request, "customer/index.html")
