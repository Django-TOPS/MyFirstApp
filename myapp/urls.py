from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name='index'),
    #path('',views.signup),
    path('profile/',views.profile,name='profile'),
    path('updatestudent/<int:id>',views.updatestudent),
    path('deleteprofile/<int:id>',views.deleteprofile),
    path('student/',views.student,name='student'),
    path('studentdata',views.studentdata),
    path('updateprofile/',views.updateprofile),
    path('user_logout',views.user_logout),
]
