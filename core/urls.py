from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('register/', views.register_patient, name='register_patient'),
    path('appointments/export/', views.export_appointments_csv, name='export_appointments'),



]
