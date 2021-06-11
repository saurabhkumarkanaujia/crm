from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Certificate, Person
from xhtml2pdf import pisa


# Create your views here.

def index(request):
    cert_id = Certificate.objects.all()
    return render(request, 'index.html', {'cert_details':cert_id})

def base(request):
    cer_id = Certificate.objects.all()
    return render(request, 'submit_line.html', {'cert':cer_id})

def add_person(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        card=request.FILES['card']
        dob=request.POST['dob']
        gender=request.POST['gender']
        type=request.POST['type']
        person_data = Person(name=name, email= email, phone=phone,card=card,dob=dob,gender=gender,type=type)
        person_data.save();
        messages.success(request,'Details Inserted')
        return redirect('person_details')
    else:
        return render(request,'add_person.html')


def person_details(request):
    data = Person.objects.all()
    return render(request, 'person_details.html', {'c_data': data})