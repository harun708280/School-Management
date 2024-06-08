from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

@login_required(login_url='/')
def Home(request):
    return render(request, 'hod/home.html')

@login_required(login_url='/')
def Add_Student(request):
    courses = Course.objects.all()
    sessions = session_year.objects.all()
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        date_of_birth = request.POST.get('date_of_brith')
        religion = request.POST.get('raligion')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course')
        session_id = request.POST.get('session')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        picture = request.FILES.get('pic')
        password = request.POST.get('password')
        address = request.POST.get('address')
        join_date = request.POST.get('join_date')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'This Email is already in use')
            return redirect('addstudent')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'This username is already in use')
            return redirect('addstudent')
        
        else:
            user = CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=picture,
                user_type=3
            )
            user.set_password(password)
            user.save()
            
            course = Course.objects.get(id=course_id)
            session = session_year.objects.get(id=session_id)
            student = Student(
                admin=user,
                address=address,
                gender=gender,
                religion=religion,
                dateOfBrith=date_of_birth,
                course_id=course,
                session_year=session,
                phone=phone,
                create_at=join_date,
            )
            student.save()
            messages.success(request, user.first_name +' '+ user.last_name + 'Are Succcesfully Added')
            return redirect('addstudent')
    
    context = {
        'courses': courses,
        'sessions': sessions,
    }

    return render(request, 'hod/addstudent.html', context)
