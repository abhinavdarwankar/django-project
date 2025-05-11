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
    path('aboutUS/',lambda request: HttpResponse("<b>ABOUT US COMPANY</B> <p>The About Us page of your website is an essential source of information for anyone who wants to know more about your business.It is where you showcase your history, the unique value of your work, your mission and vision, and the audiences you serve.Together, the design, written content, and visual elements of an About Us page tell an important story about who you are and what matters to you.</p>")),

    path('', help, name='help'),
    path('help/',lambda request: HttpResponse("<b>for help call me herry<b>")),

]