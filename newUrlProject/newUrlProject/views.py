from django.shortcuts import render
from .form import userform,calculator
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

def calculate(request):
    # Initialize variables for GET requests
        
    result = None
    form = calculator()

    if request.method == "POST":
        form = calculator(request.POST) 
        
        if form.is_valid():
            num1 = form.cleaned_data["num1"] 
            num2 = form.cleaned_data["num2"] 
            ops = form.cleaned_data["operations"]  
                  
            try:
                if ops[0] == "+":
                    result = num1 + num2
                elif ops[0] == "-":
                    result = num1 - num2
                elif ops[0] == "*":
                    result = num1 * num2
                elif ops[0] == "/":
                    result = num1 / num2
            except ZeroDivisionError:
                form.add_error("num2", "Cannot divide by zero.")
            except Exception as e:
                form.add_error(None, f"An unexpected error occurred: {e}")
            
    return render(
        request,
        "calculator.html",
        {
            "form": form,
            "result": result,  # Renamed to "result" for clarity in template
        }
    )   