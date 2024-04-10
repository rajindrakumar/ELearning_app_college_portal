from django.contrib import admin
from django.urls import path, include
from instructor import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.college_register,name="college_register"),
    path('college_dashboard/',views.college_dashboard,name="college_dashboard"),
    # path('instructor_create_course/',views.instructor_create_course,name="instructor_create_course"),
    # path('instructor_delete_account/',views.instructor_delete_account,name="instructor_delete_account"),
    # path('instructor_earning/',views.instructor_earning,name="instructor_earning"),
    # path('instructor_edit_profile/',views.instructor_edit_profile,name="instructor_edit_profile"),
    # path('instructor_list/',views.instructor_list,name="instructor_list"),
    # path('instructor_manage_course/',views.instructor_manage_course,name="instructor_manage_course"),
    # path('instructor_order/',views.instructor_order,name="instructor_order"),
    # path('instructor_payout',views.instructor_payout,name="instructor_payout"),
    # path('instructor-quiz',views.instructor_quiz,name="instructor_quiz"),
    # path('instructor_review',views.instructor_review,name="instructor_review"),
    # path('instructor_setting',views.instructor_setting,name="instructor_setting"),
    # path('instructor_single',views.instructor_single,name="instructor_single"),
    # path('instructor_studentlist',views.instructor_studentlist,name="instructor_studentlist"),
    path('college_login',views.college_login,name="college_login"),
    path('doLogout',views.doLogout,name='logout'),
    
     # profile update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),

    path('College/Home',views.COLLEGE_HOME,name='college_home'),
    path('College/Student/Add',views.ADD_STUDENT,name='add_student'),
    path('College/Student/View',views.VIEW_STUDENT,name='view_student'),
    path('College/Student/Edit/<str:id>',views.EDIT_STUDENT,name='edit_student'),
    path('College/Student/Update',views.UPDATE_STUDENT,name='update_student'),
    path('College/Student/Delete/<str:admin>',views.DELETE_STUDENT,name='delete_student'),

    path('College/WorkShop',views.COLLEGE_WORKSHOP,name='college_workshop'),

    path('College/Course/Add',views.ADD_COURSE,name='add_course'),
    path('College/Course/View',views.VIEW_COURSE,name='view_course'),
    path('College/Course/Edit/<str:id>',views.EDIT_COURSE,name='edit_course'),
    path('College/Course/Update',views.UPDATE_COURSE,name='update_course'),
    path('College/Course/Delete/<str:id>',views.DELETE_COURSE,name='delete_course'),

    path('College/MiniProject/Add',views.ADD_MINI_PROJECT,name='add_mini_project'),
    path('College/MiniProject/View',views.VIEW_MINI_PROJECT,name='view_mini_project'),
    path('College/MiniProject/Edit/<str:id>',views.EDIT_MINI_PROJECT,name='edit_mini_project'),
    path('College/MiniProject/Update',views.UPDATE_MINI_PROJECT,name='update_mini_project'),
    path('College/MiniProject/Delete/<str:id>',views.DELETE_MINI_PROJECT,name='delete_mini_project'),

    path('College/MajorProject/Add',views.ADD_MAJOR_PROJECT,name='add_major_project'),
    path('College/MajorProject/View',views.VIEW_MAJOR_PROJECT,name='view_major_project'),
    path('College/MajorProject/Edit/<str:id>',views.EDIT_MAJOR_PROJECT,name='edit_major_project'),
    path('College/MajorProject/Update',views.UPDATE_MAJOR_PROJECT,name='update_major_project'),
    path('College/MajorProject/Delete/<str:id>',views.DELETE_MAJOR_PROJECT,name='delete_major_project'),


    path('College/Session/Add',views.ADD_SESSION,name='add_session'),
    path('College/Session/View',views.VIEW_SESSION,name='view_session'),
    path('College/Session/Edit/<str:id>',views.EDIT_SESSION,name='edit_session'),
    path('College/Session/Update',views.UPDATE_SESSION,name='update_session'),
    path('College/Session/Delete/<str:id>',views.DELETE_SESSION,name='delete_session'),


    path('College/Internship/Add',views.ADD_INTERNSHIP,name='add_internship'),
    path('College/Internship/View',views.VIEW_INTERNSHIP,name='view_internship'),
    path('College/Internship/Edit/<str:id>',views.EDIT_INTERNSHIP,name='edit_internship'),
    path('College/Internship/Update',views.UPDATE_INTERNSHIP,name='update_internship'),
    path('College/Internship/Delete/<str:id>',views.DELETE_INTERNSHIP,name='delete_internship'),

    path('College/Review',views.REVIEW,name='review'),


]


