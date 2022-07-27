from django.db import models
from datatime import datatime

class Patient(models.Model):
    patient_Number=models.CharField(max_length=15,null=True,unique=True)
    registration_date=models.DateField(name=True)
    First_Name=models.CharField(max_length=14,null=True)
    Last_Name=models.CharField(max_length=13,null=True)
    date_of_birth=models.DateField()
    gender_choice=(
        ("1",'Male'),
        ("2",'Female'),
        ("3",'Others'),
    )
    gender=models.CharField(max_length=17,choices=gender_choice,null=True)
    
