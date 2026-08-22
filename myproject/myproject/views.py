from django.http import HttpResponse
from django.shortcuts import render

  

def Newpage(request):
    data = {
        "names":["rishabh","aryan","sandeep"],
        "numbers":[
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            {"name":"rishabh","phone":12345678},
            {"name":"raj","phone":334445645},
            {"name":"raj","phone":334445645},
            
            ]
        
        }
    return render(request,"index.html",data)
    