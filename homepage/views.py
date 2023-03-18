from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/homepage.html')

def documentation(request):
    return render(request, 'homepage/doc.html')
