# students/views.py
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_database')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})

def student_database(request):
    students = Student.objects.all()
    return render(request, 'students/student_database.html', {'students': students})

