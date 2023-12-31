# chatbot_app/utils.py
import requests

def get_gemini_model_response(user_input):
    # Replace 'YOUR_API_ENDPOINT' and 'YOUR_API_KEY' with actual values
    api_endpoint = 'YOUR_API_ENDPOINT'
    api_key = 'YOUR_API_KEY'
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    
    data = {
        'input': user_input,
        'context': 'optional_context',
        # Add any other required parameters
    }
    
    response = requests.post(api_endpoint, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('output')
    else:
        return 'Error processing request'
