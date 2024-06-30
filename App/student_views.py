from django.shortcuts import render,redirect

from .models import *

def studentnotificationview(request):
    student=Student.objects.filter(admin=request.user.id)
    for x in student:
        student_id=x.id
        notification=StudentNotifications.objects.filter(student=student_id)
        
    return render(request,'student/notification.html',locals())