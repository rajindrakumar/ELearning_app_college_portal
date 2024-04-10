from django.contrib import admin
from .models import *
from instructor.models import Instructor_d

admin.site.register(Instructor_d)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','full_name','email')

admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Mini_Project)
admin.site.register(Major_Project)
admin.site.register(Internship)
admin.site.register(Student)