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
    path('student/delete/<int:admin>/', hod_views.DeleteStudent, name='delete_student'),
    path('hod/student_details/<int:id>',hod_views.StudentDetails,name='student_details'),
    path('hod/add_corse/',hod_views.Add_Course,name='add_course'),
    path('hod/course_view/',hod_views.view_course,name='course_view'),
    path('hod/course_edit/<str:id>',hod_views.edit_course,name='edit_course'),
    path('ho/crouse/update/',hod_views.Update_crouse,name='course_update'),
    path('hod.couse/delate/<str:id>',hod_views.crouse_delate,name='crouse_delate'),
    path('hod/staf_add/',hod_views.StafAdd,name='stafadd'),
    path('hode/staf-view/',hod_views.Staf_view,name='stafView'),
    path('hod/staf_edit/<str:id>',hod_views.Staf_Edit,name='edit_staf'),
    path('hod/stafupdate/',hod_views.stafUpdate,name='stafupdate'),
    path('hod/staf_delate/<int:admin>/',hod_views.staf_delate,name='stafdelate'),
    path('hod/stafDetails/<int:id>/',hod_views.Staf_details,name='stafdetails'),
    path('hod/subjectadd/',hod_views.SubjectAdd,name='subjectAdd'),
    path('hod/subjctView/',hod_views.SubjectView,name='subject_view'),
    path('hod/sub-update/<int:id>/',hod_views.editSubject,name='sub-edit'),
    path('hod/update-sub,',hod_views.sub_update,name='sub-update'),
    path('staf/notification/',hod_views.stafNotifications,name='stafNotification'),
    path('staf/save/notification/',hod_views.saveStafNotification,name='staf_save_notification'),
    path('student/home/',hod_views.StudentHome,name='studenthome'),
    path('student/notifications/',hod_views.StudentNotificationView,name='studentnotifications'),
    path('student/save/notifications/',hod_views.SaveStudentNotifications,name='studentsaveNotifications'),
    
    #Staf Urls 
    
    path('staf/home/',staf_views.StafView,name='stafhome'),
    path('staf/Notification',staf_views.StafViewNotification,name='notification'),
    path('staf/markasdone/<str:status>',staf_views.Noti_mark_done,name='morkdoneNotifications'),
    
    #studnet Notifications
    
    path('st/notifications/bd/',student_views.studentnotificationview,name='notificationsStudent_check'),
    path('student/notification/markdone/<str:student_status>',student_views.studentnotificationsmarkdone,name='student_notificationmark_done'),
    
    
    

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
