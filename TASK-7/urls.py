# urls.py
from django.urls import path
from .views import edit_student, delete_student

urlpatterns = [
    # Other patterns
    path('edit/<int:student_id>/', edit_student, name='edit_student'),
    path('delete/<int:student_id>/', delete_student, name='delete_student'),
]

