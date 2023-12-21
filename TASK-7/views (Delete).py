# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('home')  # Redirect to the home page or any other appropriate page
    return render(request, 'delete_student.html', {'student': student})

