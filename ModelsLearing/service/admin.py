from django.contrib import admin
from service.models import Service,FavYoutuber

class ServiceModel(admin.ModelAdmin):
    thing = ('name','salary','discreption')

admin.site.register(Service,ServiceModel)


class Favyoutuber(admin.ModelAdmin):
    YourYoutuber = ('name','subcribers')

admin.site.register(FavYoutuber,Favyoutuber)






