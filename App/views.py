from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from.EmailBackEnd import *
from.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
# Create your views here.
def base(request):
    return render(request,'base.html')

def Login(request):
    return render(request,'login.html')

def Dologin(request: HttpRequest):
    if request.method == 'POST':
        backend = EmailBackend()
        user = backend.authenticate(request,
                                    username=request.POST.get('email'),
                                    password=request.POST.get('password'),)
        
        if user is not None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hode/home')
            elif user_type == '2':
                return redirect('stafhome')
            elif user_type == '3':
                return HttpResponse('This is student panel')
            else:
                messages.error(request,' Email And Password Invalid ')
                return redirect('login')
        else:
            messages.error(request,' Email And Password Invalid ')
            return redirect('login')
    else:
        return HttpResponse('Invalid request method', status=405)

def DoLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def Profile(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
        context = {
            'user': user
        }
        return render(request, 'profile.html', context)
    except CustomUser.DoesNotExist:
        messages.error(request, 'User does not exist.')
        return redirect('login')  # or any other appropriate view

@login_required(login_url='/')
def UpdateProfile(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            if profile_pic:
                customuser.profile_pic = profile_pic
            if password:
                customuser.set_password(password)
            customuser.save()
            messages.success(request, 'Your profile was updated successfully')
            return redirect('profile')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Failed to update profile.')
            return redirect('profile')
    return render(request, 'profile.html')