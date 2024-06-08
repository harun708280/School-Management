from django.urls import path
from.import views,hod_views,staf_views,student_views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('base',views.base),
    #login Pathh
    path('',views.Login,name='login'),
    path('dologin/',views.Dologin,name='dologin'),
    path('dolgout/',views.DoLogout,name='logout'),
    
    #profile Upddate
    
    path('updateprofile/', views.UpdateProfile, name='updateprofile'),
    path('profile/', views.Profile, name='profile'),
    
    #Hod Section Urls
    path('hode/home',hod_views.Home,name='hode/home'),
    path('hod/StudentAdd/',hod_views.Add_Student,name='addstudent'),
    path('hode/viewStuent/',hod_views.StuddentView,name='viewStudent'),
    path('hode/StudentEdit/<str:id>',hod_views.Student_Edit,name='student_edit'),
    path('studentUpadate/',hod_views.StudentUpdate,name='updateStudent'),
    path('student/delete/<int:admin>/', hod_views.DeleteStudent, name='delete_student')

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
