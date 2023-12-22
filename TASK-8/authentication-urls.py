# authentication/urls.py
from django.urls import path
from .views import login_view, signup_view, student_database_view, signout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('student-database/', student_database_view, name='student_database'),
    path('signout/', signout_view, name='signout'),
]
