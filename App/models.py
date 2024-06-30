from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER=(
        (1, 'HOD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),
    )
    user_type=models.CharField(choices=USER, max_length=50,default=1,blank=True,null=True)
    profile_pic=models.ImageField( upload_to='profile pic',blank=True,null=True)
    
class Course(models.Model):
    name=models.CharField( max_length=50)
    created_date=models.DateField( auto_now_add=True)
    update_date=models.DateField( auto_now=True)
    
    def __str__(self):
        return self.name

class session_year(models.Model):
    session_start=models.CharField( max_length=100)
    session_end=models.CharField( max_length=100)
    
    def __str__(self):
        return self.session_start
    
    
class Student(models.Model):
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address=models.TextField()
    gender=models.CharField(max_length=50)
    religion=models.CharField( max_length=50)
    dateOfBrith=models.DateTimeField( auto_now_add=False)
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    session_year=models.ForeignKey(session_year, on_delete=models.CASCADE)
    create_at=models.DateTimeField( auto_now_add=False)
    update_at=models.DateTimeField( auto_now=True)
    phone=models.CharField( max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.admin.first_name+ ''+self.admin.last_name
    
class Staf(models.Model):
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    address=models.CharField( max_length=50)
    gender=models.CharField( max_length=50)
    religion=models.CharField( max_length=50)
    univercity=models.CharField( max_length=50)
    subject=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    create=models.DateField( auto_now_add=False)
    update=models.DateField( auto_now=True)
    def __str__(self):
        return self.admin.username
    
    
class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    staf_name = models.ForeignKey(Staf, on_delete=models.CASCADE, related_name='subjects')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.subject_name
    
class stafNotificatuion(models.Model):
    
    staf_id=models.ForeignKey(Staf, on_delete=models.CASCADE)
    message=models.TextField()
    crated_at=models.DateTimeField( auto_now_add=True)
    status=models.IntegerField(null=True,default=0)
    def __str__(self):
        return self.staf_id.admin.first_name
    
    def mark_done(self):
        self.status = 1
        self.save()
        

class StudentNotifications(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    message=models.TextField()
    status=models.IntegerField(default=0,null=True)
    create_at=models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.student.admin.username
    
    def student_markdone(self):
        self.status = 1
        self.save()
    
    