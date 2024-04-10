import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.
class Instructor_d(AbstractUser):
    CollegeName = models.CharField( max_length=122)
    CollegeCode=models.CharField(max_length=50)
    adminAdministrator=models.CharField(max_length=122)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=120)
    address = models.TextField(default='DEFAULT VALUE', blank=True, null=True)
    aboutcollege = models.TextField(default='DEFAULT VALUE', blank=True, null=True)
    profile_pic = models.ImageField(upload_to='media/profile_pic',blank=True, null=True)
    

    def __str__(self):
        return self.CollegeName

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[email]
    objects=UserManager()

defult = None
# Create Course and session Model  
  
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Session_Year(models.Model):
    session_start = models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)


    def __str__(self):
        return self.session_start + " To " + self.session_end
    
class Mini_Project(models.Model):
    mini_project_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mini_project_name
    

class Major_Project(models.Model):
    major_project_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.major_project_name
    

class Internship(models.Model):
    internship_name = models.CharField(max_length=100)
    internship_start = models.CharField(max_length=100)
    internship_end = models.CharField(max_length=100)


    def __str__(self):
        return self.internship_name


# Create Student Model
class Student(models.Model):
    admin = models.OneToOneField(Instructor_d,on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    internship_id = models.ForeignKey(Internship,on_delete=models.DO_NOTHING)
    major_project_id = models.ForeignKey(Major_Project,on_delete=models.DO_NOTHING)
    mini_project_id = models.ForeignKey(Mini_Project,on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(Session_Year,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # profile_pic = models.ImageField(upload_to='media/profile_pic')

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
   



