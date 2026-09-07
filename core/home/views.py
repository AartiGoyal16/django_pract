from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples=[
        {'name':'Aarti','age':2},
        {'name':'Aarti1','age':261},
        {'name':'Aarti2','age':262},
        {'name':'Aarti3','age':263},
        {'name':'Aarti4','age':264},
    ]
    
    line="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi diam."
    return render(request,"index.html",context={'people':peoples,'text':line})

def success_page(request):
    print('*'*10)
    return HttpResponse("<h1>Hi this is success page</h1>")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")