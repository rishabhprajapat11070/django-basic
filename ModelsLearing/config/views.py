from django.shortcuts import render
from service.models import FavYoutuber


def home(request):
    return render(request,"about.html")

def your_youtuber(request):
    listOfyoutuber = FavYoutuber.objects.all()
    for i in listOfyoutuber:
        print(i.name)
    return render(request,'fav.html',{'youtuber':listOfyoutuber})
    