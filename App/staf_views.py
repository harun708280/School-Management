from django.shortcuts import render,redirect

def StafView(request):
    
    return render(request,'staf/home.html')