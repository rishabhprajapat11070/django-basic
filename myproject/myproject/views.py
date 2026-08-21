from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("whelcome to rishabh website ")
    
def calculatr(request,a,b):
    sum = a+b
    return HttpResponse(f"Hello {sum}")