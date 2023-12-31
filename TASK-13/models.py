# chatbot_app/models.py
from django.db import models

class Conversation(models.Model):
    user_input = models.TextField()
    model_output = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
