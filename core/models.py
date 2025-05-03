from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    available_days = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.name} with Dr. {self.doctor.name} on {self.appointment_date}"
