from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm, PatientForm
from .models import Appointment

def home(request):
    return render(request, 'core/home.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('book_appointment')
    else:
        form = AppointmentForm()
    return render(request, 'core/book.html', {'form': form})

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient registered successfully!')
            return redirect('register_patient')
    else:
        form = PatientForm()
    return render(request, 'core/register_patient.html', {'form': form})

def appointment_list(request):
    doctor_name = request.GET.get('doctor', '')
    if doctor_name:
        appointments = Appointment.objects.filter(doctor__name__icontains=doctor_name)
    else:
        appointments = Appointment.objects.all().order_by('appointment_date')
    return render(request, 'core/appointments.html', {'appointments': appointments, 'doctor_name': doctor_name})
import csv
from django.http import HttpResponse

def export_appointments_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="appointments.csv"'

    writer = csv.writer(response)
    writer.writerow(['Doctor', 'Patient', 'Date & Time'])

    appointments = Appointment.objects.all()
    for appt in appointments:
        writer.writerow([appt.doctor.name, appt.patient.name, appt.appointment_date])

    return response
