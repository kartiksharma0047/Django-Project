from django.shortcuts import render
# Create your views here.

def home(request):
    # Lets Try Django template engine (We want to display peoples data into our html from server)
    peoples=[
        {'name':'Kartik','age':21},
        {'name':'Baman','age':16},
        {'name':'Diya','age':20},
        {'name':'Ravi','age':25},
        {'name':'Raju','age':10},
        {'name':'pushpa','age':56},
        {'name':'Goremon','age':9},
    ]
    return render(request,"home_folder/index.html",context={"peoples":peoples,'page':'Home Page'})

def contact(request):
    context= {'page':'Contact Page'}
    return render(request,"home_folder/contact.html",context)

def about(request):
    context= {'page':'About Page'}
    return render(request,"home_folder/about.html",context)