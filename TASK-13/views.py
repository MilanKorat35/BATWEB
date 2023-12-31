# chatbot_app/views.py
from django.shortcuts import render
from .models import Conversation
from .utils import get_gemini_model_response

def chat(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        model_output = get_gemini_model_response(user_input)
        Conversation.objects.create(user_input=user_input, model_output=model_output)

    conversations = Conversation.objects.all()
    return render(request, 'chatbot_app/chat.html', {'conversations': conversations})
