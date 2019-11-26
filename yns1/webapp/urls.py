from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('course',views.course,name='course'),
    path('coursesci',views.coursesci,name='coursesci'),
    path('coursemath',views.coursemath,name='coursemath'),
    path('coursesocial',views.coursesocial,name='courseso'),
    path('coursethai',views.thai,name='thai'),
    path('courseeng',views.eng,name='eng'),
    path('about',views.about,name='about'),
    path('coursedetail/<itemID>',views.coursedetail,name='coursedetail'),
    path('exam/<itemID>',views.exam,name='exam'),
    path('checkAnswer/',views.checkanswer,name='checkAnswer')
]
