from django.shortcuts import render
from .models import*
import openai, requests
from django.http import HttpResponse
# from openai import OpenAI
import os

# Create your views here.

def home(request):
    # Send the request to the OpenAI API
    if request.method == 'POST':
        question = request.POST.get('question')
        # Call OpenAI API
        openai.api_key = ("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")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=2500,
            temperature=0.9,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["500000"]
        )
        answer = response['choices'][0].text # Get the response from the API
        print(answer)
        return render(request, 'home.html', {'answer': answer})
    return render(request, 'home.html')


    
