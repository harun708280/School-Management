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


def StuddentView(request):
    studdent=Student.objects.all().order_by('-id')
    context={
        'student':studdent
    }
    return render(request,'hod/view_student.html',context)

def Student_Edit(request,id):
    student=Student.objects.filter(id=id)
    courses = Course.objects.all()
    sessions = session_year.objects.all()
    
    context={
        'student':student,
        'course':courses,
        'session':sessions,
    }
    
    return render(request,'hod/student_edit.html',context)

def StudentUpdate(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        religion = request.POST.get('raligion')  
        gender = request.POST.get('gender')
        course_id = request.POST.get('course')
        session = request.POST.get('session')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        profile_pic = request.FILES.get('pic')
        password = request.POST.get('password')
        address = request.POST.get('address')
        
        # Update CustomUser
        user = CustomUser.objects.get(id=student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        if profile_pic:
            user.profile_pic = profile_pic
        if password:
            user.set_password(password)
        user.save()
        
        # Update Student
        student = Student.objects.get(admin=user)
        course = Course.objects.get(id=course_id)
        session=session_year.objects.get(id=session)
        student.address = address
        student.religion = religion
        student.gender = gender
        student.course_id = course 
        student.session_year=session
        student.phone=phone
        student.save()
        messages.success(request,'succesfully Edit Now' +user.first_name + ' '+ user.last_name)
        
        return redirect('viewStudent')
    else:
        messages.warning(request,'Something Went Wrong')
        return redirect('updateStudent')
        
def DeleteStudent(request, admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request, 'Successfully deleted student ' )
    return redirect('viewStudent')

def StudentDetails(request,id):
    student=Student.objects.get(id=id)
    return render(request,'hod/studentdetail.html',locals())


def Add_Course(request):
    if request.method=='POST':
        cours_name=request.POST.get('course')
        
        course=Course(
            name=cours_name
        )
        course.save()
        messages.success(request,'Course are succesfully create '  )
        return redirect('course_view')
    # else :
    #     messages.warning(request,'Something went wrong')
    #     return redirect('add_course')
    return render(request,'hod/add_course.html')

def view_course(request):
    coures=Course.objects.all().order_by('-id')
    context={
        'course':coures,
    }
    
    return render(request,'hod/course_view.html',context)

def edit_course(request,id):
    course=Course.objects.get(id=id)
    context={
        'c':course,
    }
    return render(request,'hod/edit_course.html',context)

def Update_crouse(request):
    if request.method == 'POST':
        course=request.POST.get('course_name')
        course_id=request.POST.get('course_id')
        
        course_name=Course.objects.get(id=course_id)
        
        course_name.name=course
        course_name.save()
        
        messages.success(request,'SucessFully Update ' + course_name.name )
        
        return redirect('course_view')
        
def crouse_delate(request,id):
    course=Course.objects.get(id=id) 
    course.delete()  
    messages.success(request,'Sucessfuily Delate')
    return redirect('course_view')

def StafAdd(request):
    if request.method== 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        raligion=request.POST.get('raligion')
        univercity=request.POST.get('univercity')
        subject=request.POST.get('subject')
        gender=request.POST.get('gender')
        join_date=request.POST.get('join_date')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        picture=request.FILES.get('pic')
        address=request.POST.get('address')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'This username Already Used')
            return redirect('stafadd')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'sorry this email already used')
            return redirect('stafadd')
        
        else:
            staf_user=CustomUser(
                
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                user_type=2,
                profile_pic=picture     
            )
            
            staf_user.set_password(password)
            staf_user.save()
            
            staf=Staf(
                admin=staf_user,
                address=address,
                gender=gender,
                religion=raligion,
                univercity=univercity,
                subject=subject,
                phone=phone,
                create=join_date
            )
            staf.save()
            messages.success(request,'Sucessfully Added by '+staf_user.first_name+ ' '+staf_user.last_name)
            return redirect('stafadd')
        
        
    
        
    return render(request,'hod/add_staf.html')


