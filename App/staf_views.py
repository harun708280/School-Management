from django.shortcuts import render,redirect
from.models import *
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