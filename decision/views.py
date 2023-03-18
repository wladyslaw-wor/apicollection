from django.shortcuts import render
import requests

def decision(request):
    r = requests.get('https://yesno.wtf/api')
    answer = r.json()['answer']
    gif = r.json()['image']
    return render(request, 'decision/result.html', {'gif': gif, 'answer': answer})

