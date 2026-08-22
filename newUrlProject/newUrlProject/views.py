from django.shortcuts import render

def home(request):
    return render(request ,"Index.html")    
def about(request):
    return render(request ,"about.html")    
def resume(request):
    return render(request ,"resume.html")    