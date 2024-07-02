from django.shortcuts import render,redirect

from .models import *

def studentnotificationview(request):
    student=Student.objects.filter(admin=request.user.id)
    for x in student:
        student_id=x.id
        notification=StudentNotifications.objects.filter(student=student_id).order_by('-id')
        
    return render(request,'student/notification.html',locals())

def studentnotificationsmarkdone(request,student_status):
    notification=StudentNotifications.objects.get(id=student_status)
    notification.student_markdone()
    return redirect('notificationsStudent_check')