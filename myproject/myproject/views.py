from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return render(request,"about.html")
    

def home(request):
    return render(request,"index.html")
    