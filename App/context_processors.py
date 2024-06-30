# In your app's context_processors.py file

from .models import Staf, stafNotificatuion

def StafViewNotification(request):
    c = 0  
    
    if request.user.is_authenticated: 
        staf = Staf.objects.filter(admin=request.user.id)
        
        for i in staf:
            staf_id = i.id
            notifications = stafNotificatuion.objects.filter(staf_id=staf_id, status=0)
            c += notifications.count()  # 
    
    return {'c': c}
