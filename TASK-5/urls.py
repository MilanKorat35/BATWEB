# resumeapp/urls.py

from django.urls import path
from .views import resume

urlpatterns = [
    path('resume/', resume, name='resume'),
    # Add other URL patterns as needed
]
