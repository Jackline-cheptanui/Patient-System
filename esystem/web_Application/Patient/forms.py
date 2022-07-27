from dataclasses import field
from pyexpat import model
from django import forms
from.models import Patient
class PatientRegistrationForms(forms.ModelForm):
  class Meta:
    model=Patient
    field="__ all__"