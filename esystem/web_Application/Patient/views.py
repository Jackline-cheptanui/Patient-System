import imp
from django.shortcuts import render
from.models import Patient
from django import forms
from django.shortcuts import redirect,render
from.forms import PatientRegistrationForms

def register_patient(request):
    if request.method=="POST":
        form=PatientRegistrationForms(request.POST,request.FILES,)
        if forms.is_valid():
            form.save()
        else:
                print(form.errors)
    else:
                form=PatientRegistrationForms()
                return render(request,"register_patient.html",{"form":form})
                