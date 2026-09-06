from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples=[
        {'name':'Aarti','age':26},
        {'name':'Aarti1','age':261},
        {'name':'Aarti2','age':262},
        {'name':'Aarti3','age':263},
        {'name':'Aarti4','age':264},
    ]
    return render(request,"index.html",context={'people':peoples})

def success_page(request):
    print('*'*10)
    return HttpResponse("<h1>Hi this is success page</h1>")