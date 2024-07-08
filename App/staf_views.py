from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
def StafView(request):
    
    return render(request,'staf/home.html')

def StafViewNotification(request):
    staf=Staf.objects.filter(admin=request.user.id)
    
    for i in staf:
        staf_id=i.id
        
        notification=stafNotificatuion.objects.filter(staf_id=staf_id).order_by('-id')
        notifications = stafNotificatuion.objects.filter(staf_id=staf_id, status=0)
        count = notifications.count()
        
        print(count)
    
    return render(request,'staf/notification.html',locals())

def Noti_mark_done(request,status):
    notification=stafNotificatuion.objects.get(id=status)
    notification.mark_done()
    
    return redirect('notification')

def StafApplyLeave(request):
    staf=Staf.objects.filter(admin = request.user.id)
    for x in staf:
        staf_id=x.id
        leave_history=Stafleave.objects.filter(staf_id=staf_id)
        
    return render(request,'staf/leave.html',locals())



def leaveSave(request):
    if request.method == "POST":
        leavedate=request.POST.get('leavedate')
        message=request.POST.get('message')
        staf_id=Staf.objects.get(admin=request.user.id)
        
        leave=Stafleave(
           staf_id=staf_id,
            data=leavedate,
            message=message
        ).save()
        messages.success(request,"Succesfully sent Apply your Leave")
        
        
        
    return redirect('stafleave')