# students/urls.py
from django.urls import path
from .views import student_form, student_database

urlpatterns = [
    path('student_form/', student_form, name='student_form'),
    path('student_database/', student_database, name='student_database'),
]

