from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        'title': 'homepage',
        'bdata': 'welcome to abhinav',
        'clist': ['abhinav', 'ganesh', 'kartik'],
        'dlist': ['raghav', 'avery', 'arohi'],
        'student_detail': [
            {'name': 'abhinav', 'phone': 9689445654},
            {'name': 'raghav', 'phone': 9689445656},
        ]
    }
    return render(request, "index.html", data)

def aboutUS(request):
    return HttpResponse("About Us page")
