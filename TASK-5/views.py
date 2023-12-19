# resumeapp/views.py

from django.shortcuts import render

def resume(request):
    resume_data = {
        'name': 'Your Name',
        'skills': ['Skill 1', 'Skill 2', 'Skill 3'],
        # ... other resume data
    }
    return render(request, 'resumeapp/resume.html', {'resume_data': resume_data})

