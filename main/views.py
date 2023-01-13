from django.shortcuts import render
from .models import*
import openai, requests
from django.http import HttpResponse
# from openai import OpenAI

# Create your views here.

def home(request):
    # Send the request to the OpenAI API
    if request.method == 'POST':
        question = request.POST.get('question')
        # Call OpenAI API
        openai.api_key = "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"
        response = openai.Completion.create(
            engine="davinci-instruct-beta",
            prompt=question,
            max_tokens=100,
            temperature=0.1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        answer = response['choices'][0].text # Get the response from the API
        return render(request, 'home.html', {'answer': answer})
    return render(request, 'home.html')


    
