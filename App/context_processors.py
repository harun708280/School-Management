# In your app's context_processors.py file

from .models import *

def StafViewNotification(request):
    c = 0  
    
    if request.user.is_authenticated: 
        staf = Staf.objects.filter(admin=request.user.id)
        
        for i in staf:
            staf_id = i.id
            notifications = stafNotificatuion.objects.filter(staf_id=staf_id, status=0)
            c += notifications.count()  # 
    
    return {'c': c}

# def Studentunsennotifications(request):
#     if request.user.is_authenticated:
#      student=Student.objects.filter(admin=request.user.id)
#      for x in student:
#          student_id=x.id
#          notificationcount=StudentNotifications.objects.filter(student=student_id,status=0).count()
         
#     return {'notic':notificationcount}
