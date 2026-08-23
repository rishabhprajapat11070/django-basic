from django.shortcuts import render
from .form import userform
import sys

def home(request):
    return render(request ,'index.html')  
 
def about(request):
    return render(request ,"about.html") 
   
def resume(request):
    return render(request ,"resume.html")  
  
def form(request):
    Form = userform()
    try:
        print(request.POST.get("num1"))
        print(request.POST.get("num2"))
        print(request.POST.get("gender"))
    except Exception as e:
        print(e)
        
    return render(request ,"from.html",{"data":Form})    