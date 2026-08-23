from django.shortcuts import render

def home(request):
    return render(request ,'index.html')  
 
def about(request):
    return render(request ,"about.html") 
   
def resume(request):
    return render(request ,"resume.html")  
  
def form(request):
    try:
        a  = request.GET.get("username")
        b  = request.GET.get("sirname")
        yourans = f"hello dear {a} {b}"
    except Exception as e:
        print(e)
    return render(request ,"from.html" ,{"ans":f"hello sir how are you {yourans}"})    