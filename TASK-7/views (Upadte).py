# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm  # Assuming you have a form for the Student model

def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_details', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form, 'student': student})

