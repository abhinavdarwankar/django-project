from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from abhiproject import views


def aboutus(request):
    return HttpResponse("welcome")

def help(request):
    return HttpResponse() 


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.homepage),
    

    
    path('', aboutus, name='aboutus'),
    path('aboutUS/',lambda request: HttpResponse("<b> xxxx <b>")),

    path('', help, name='help'),
    path('help/',lambda request: HttpResponse("<b>for help call me herry<b>")),

]