from django.shortcuts import render
from .models import*
import openai, requests
from django.http import HttpResponse
# from openai import OpenAI
import os
from dotenv import load_dotenv

# Create your views here.

def home(request):
    load_dotenv()
    # Send the request to the OpenAI API
    if request.method == 'POST':
        question = request.POST.get('question')
        # Call OpenAI API
        openai.api_key = os.environ.get("api_key")
        # openai.api_key = ("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")
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


    
