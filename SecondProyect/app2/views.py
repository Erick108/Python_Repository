from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def laptop(request):
    return render(request, 'laptop.html')
