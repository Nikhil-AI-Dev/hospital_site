from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact']
