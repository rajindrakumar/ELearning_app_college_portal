from django.shortcuts import render, HttpResponse ,redirect
from instructor.models import Instructor_d
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth import get_user_model
from instructor.models import Course,Session_Year,Major_Project,Mini_Project,Student,Internship
# ,Student_Feedback,Staff,Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Student_Notification,Student_Leave,Attendance_Report,Attendance,StudentResult

User=get_user_model
def college_register(request):
    if request.method =="POST":
        
        CollegeName= request.POST['CollegeName']
        CollegeCode=request.POST['CollegeCode']
        adminAdministrator=request.POST['adminAdministrator']
        
        email= request.POST['email']
        phone = request.POST['phone']
        password= request.POST['password']
        
        myuser=Instructor_d(email=email,CollegeName=CollegeName,CollegeCode=CollegeCode,adminAdministrator=adminAdministrator,phone=phone,password=password,username=email)
        myuser.set_password(password)
        myuser.save()
        return redirect('college_login')
    return render(request,"college_register.html")

def college_login(request):
    if request.method =="POST":
        login_email= request.POST['login_email']
        login_password= request.POST['login_password']
        user=authenticate(email=login_email,password=login_password)

        if user is not None:
            login(request,user)
            messages.success(request,"success")
            return redirect ('college_dashboard')
        else:
            messages.error(request,"invalid")
            return redirect('college_login')

    return render(request,"college_login.html")

def doLogout(request):
    logout(request)
    return redirect('college_login')

def college_dashboard(request):
    return render(request,"college-dashboard.html")


def PROFILE(request):
    return render(request,'profile.html')


def PROFILE_UPDATE(request):
    if request.method =="POST":
        
        CollegeName= request.POST['CollegeName']
        CollegeCode=request.POST['CollegeCode']
        adminAdministrator=request.POST['adminAdministrator']
        
        email= request.POST['email']
        phone = request.POST['phone']
        password= request.POST['password']
        address= request.POST['address']
        aboutcollege= request.POST['aboutcollege']
        try:
            if request.FILES['upload']:
                profile_pic = request.FILES['profile_pic']
        except:
            pass

        try:
            myuser=Instructor_d(
                profile_pic=profile_pic,
                aboutcollege=aboutcollege,
                address=address,
                CollegeName=CollegeName,
                CollegeCode=CollegeCode,
                adminAdministrator=adminAdministrator,
                phone=phone,
                password=password,
                )
             
            if password !=None and password != "":
                myuser.set_password(password)
            if profile_pic !=None and profile_pic != "":
                myuser.profile_pic = profile_pic
            myuser.save()
            messages.success(request,'Your Profile Updated Successfully !')
            return redirect('profile')
        except:
            messages.error(request,'Failed To Update Your Profile')
    
    return render(request,'profile.html')


def COLLEGE_HOME(request):
        
        student_count = Student.objects.all().count()
        course_count = Course.objects.all().count()
        mini_project_count = Mini_Project.objects.all().count()
        major_project_count = Major_Project.objects.all().count()
        internship_count = Internship.objects.all().count()

        context = {

        'student_count':student_count,
        'course_count':course_count,
        'mini_project_count':mini_project_count,
        'major_project_count':major_project_count,
        'internship_count':internship_count,

        }
        return render(request,'college_home.html',context)



def ADD_STUDENT(request):
    course = Course.objects.all()
    major_project = Major_Project.objects.all()
    mini_project = Mini_Project.objects.all()
    internship = Internship.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        internship_id = request.POST.get('internship_id')
        major_project_id = request.POST.get('major_project_id')
        mini_project_id = request.POST.get('mini_project_id')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if Instructor_d.objects.filter(email=email).exists():
           messages.warning(request,'Email Is Already Taken')
           return redirect('add_student')
        else:
            user = Instructor_d(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id=course_id)
            session_year = Session_Year.objects.get(id=session_year_id)
            mini_project = Mini_Project.objects.get(id=mini_project_id)
            major_project = Major_Project.objects.get(id=major_project_id)
            internship = Internship.objects.get(id=internship_id)

            student = Student(
                admin = user,
                address = address,
                internship_id = internship,
                major_project_id = major_project,
                mini_project_id = mini_project,
                session_year_id = session_year,
                course_id = course,
                gender = gender,
            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Are Successfully Added !")
            return redirect('add_student')



    context = {
        'course':course,
        'session_year':session_year,
        'mini_project':mini_project,
        'major_project':major_project,
        'internship':internship,
    }

    return render(request,'add_student.html',context)


def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request,'view_student.html',context)


def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    course = Course.objects.all()
    major_project = Major_Project.objects.all()
    mini_project = Mini_Project.objects.all()
    internship = Internship.objects.all()
    session_year = Session_Year.objects.all()

    context = {
        'student':student,
        'course':course,
        'session_year':session_year,
        'mini_project':mini_project,
        'major_project':major_project,
        'internship':internship,
    }
    return render(request,'edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')

        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        internship_id = request.POST.get('internship_id')
        major_project_id = request.POST.get('major_project_id')
        mini_project_id = request.POST.get('mini_project_id')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user = Instructor_d.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        mini_project = Mini_Project.objects.get(id = mini_project_id)
        student.mini_project_id = mini_project

        major_project = Major_Project.objects.get(id = major_project_id)
        student.major_project_id = major_project

        internship = Internship.objects.get(id = internship_id)
        student.internship_id = internship

        session_year = Session_Year.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Record Are Successfully Updated !')
        return redirect('view_student')

    return render(request,'edit_student.html')

def DELETE_STUDENT(request,admin):
    student = Instructor_d.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record Are Successfully Deleted !')
    return redirect('view_student')

def COLLEGE_WORKSHOP(request):
    return render(request,'college_workshop.html')



def ADD_COURSE(request):

    if request.method == "POST":
        course_name = request.POST.get('course_name')

        course = Course(
            name = course_name,
        )
        course.save()
        messages.success(request,'Course Are Successfully Created ')

        return redirect('add_course')

    return render(request,'add_course.html')


def VIEW_COURSE(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request,'view_course.html',context)


def EDIT_COURSE(request,id):
    course = Course.objects.get(id = id)

    context = {
        'course':course,
    }
    return render(request,'edit_course.html',context)

def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id = request.POST.get('course_id')

        course = Course.objects.get(id = course_id)
        course.name = name
        course.save()
        messages.success(request,'Course Are Successfully Updated')
        return redirect('view_course')

    return render(request,'edit_course.html')



def DELETE_COURSE(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request,'Course are Successfully Deleted')

    return redirect('view_course')



def ADD_MINI_PROJECT(request):

    if request.method == "POST":
        miniproject_name = request.POST.get('miniproject_name')

        mini_project = Mini_Project(
            mini_project_name = miniproject_name,
        )
        mini_project.save()
        messages.success(request,'Course Are Successfully Created ')

        return redirect('add_mini_project')

    return render(request,'add_mini_project.html')



def VIEW_MINI_PROJECT(request):
    mini_project = Mini_Project.objects.all()
    context = {
        'mini_project':mini_project,
    }
    return render(request,'view_mini_project.html',context)


def EDIT_MINI_PROJECT(request,id):
    mini_project = Mini_Project.objects.get(id = id)

    context = {
        'mini_project':mini_project,
    }
    return render(request,'edit_mini_project.html',context)


def UPDATE_MINI_PROJECT(request):
    if request.method == 'POST':
        mini_project_name = request.POST.get('mini_project_name')
        mini_project_id = request.POST.get('mini_project_id')

        mini_project = Mini_Project.objects.get(id = mini_project_id)
        mini_project.mini_project_name = mini_project_name
        mini_project.save()
        messages.success(request,'Course Are Successfully Updated')
        return redirect('view_mini_project')

    return render(request,'edit_mini_project.html')



def DELETE_MINI_PROJECT(request,id):
    mini_project = Mini_Project.objects.get(id = id)
    mini_project.delete()
    messages.success(request,'Course are Successfully Deleted')

    return redirect('view_mini_project')




def ADD_MAJOR_PROJECT(request):

    if request.method == "POST":
        majorproject_name = request.POST.get('majorproject_name')

        major_project = Major_Project(
            major_project_name = majorproject_name,
        )
        major_project.save()
        messages.success(request,'Course Are Successfully Created ')

        return redirect('add_major_project')

    return render(request,'add_major_project.html')



def VIEW_MAJOR_PROJECT(request):
    major_project = Major_Project.objects.all()
    context = {
        'major_project':major_project,
    }
    return render(request,'view_major_project.html',context)


def EDIT_MAJOR_PROJECT(request,id):
    major_project = Major_Project.objects.get(id = id)

    context = {
        'major_project':major_project,
    }
    return render(request,'edit_major_project.html',context)


def UPDATE_MAJOR_PROJECT(request):
    if request.method == 'POST':
        major_project_name = request.POST.get('major_project_name')
        major_project_id = request.POST.get('major_project_id')

        major_project = Major_Project.objects.get(id = major_project_id)
        major_project.major_project_name = major_project_name
        major_project.save()
        messages.success(request,'Course Are Successfully Updated')
        return redirect('view_major_project')

    return render(request,'edit_major_project.html')



def DELETE_MAJOR_PROJECT(request,id):
    major_project = Major_Project.objects.get(id = id)
    major_project.delete()
    messages.success(request,'Course are Successfully Deleted')

    return redirect('view_major_project')



def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end,
        )
        session.save()
        messages.success(request,'Session is successfully Added')
        return redirect('add_session')


    return render(request,'add_session.html')


def VIEW_SESSION(request):
    session = Session_Year.objects.all()

    context = {
        'session':session,
    }
    return render(request,'view_session.html',context) 


def EDIT_SESSION(request, id):
    session = Session_Year.objects.filter(id=id)

    context = {
        'session':session ,
    }
    return render(request,'edit_session.html',context)


def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
            id = session_id,
            session_start = session_year_start,
            session_end = session_year_end,

        )
        session.save()
        messages.success(request,'Session is sucessfully Updated !')
        return redirect('view_session')
    
    return render(request,'edit_session.html')


def DELETE_SESSION(request,id):
    session = Session_Year.objects.get(id=id)
    session.delete()
    messages.success(request,'Session is successfully deleted !')
    return redirect('view_session')



def ADD_INTERNSHIP(request):
    if request.method == "POST":
        internshipname = request.POST.get('internshipname')
        internship_start_date = request.POST.get('internship_start_date')
        internship_end_date = request.POST.get('internship_end_date')

        internship = Internship(
            internship_name = internshipname,
            internship_start =  internship_start_date,
            internship_end = internship_end_date,
        )
        internship.save()
        messages.success(request,'Internship is successfully Added')
        return redirect('add_internship')


    return render(request,'add_internship.html')


def VIEW_INTERNSHIP(request):
    internship = Internship.objects.all()

    context = {
        'internship':internship,
    }
    return render(request,'view_internship.html',context)


def EDIT_INTERNSHIP(request, id):
    internship = Internship.objects.filter(id=id)

    context = {
        'internship':internship ,
    }
    return render(request,'edit_internship.html',context)

def UPDATE_INTERNSHIP(request):
    if request.method == "POST":
        internship_id = request.POST.get('internship_id')
        internship_start_date = request.POST.get('internship_start_date')
        session_year_end = request.POST.get('session_year_end')

        internship = Internship(
            id = internship_id,
            internship_start = internship_start_date,
            internship_end = session_year_end,

        )
        internship.save()
        messages.success(request,'internship is sucessfully Updated !')
        return redirect('view_internship')
    
    return render(request,'edit_internship.html')


def DELETE_INTERNSHIP(request,id):
    internship = Internship.objects.get(id=id)
    internship.delete()
    messages.success(request,'internship is successfully deleted !')
    return redirect('view_internship')

def REVIEW(request):
    return render(request,'review.html')