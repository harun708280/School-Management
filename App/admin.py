from django.contrib import admin
from.models import *
from django.contrib.auth.admin import UserAdmin
# class UserModel(UserAdmin):
#     list_display=['username','user_type']
admin.site.register(CustomUser),
admin.site.register(Course),
admin.site.register(session_year),
admin.site.register(Student),
admin.site.register(Staf),
admin.site.register(Subject),
admin.site.register(stafNotificatuion),
admin.site.register(StudentNotifications),
admin.site.register(Stafleave),
# Register your models here.
