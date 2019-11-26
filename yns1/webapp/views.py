from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def course(request):
    allCourse=Course.objects.all
    return render(request,'course.html',{'data':allCourse})

def about(request):
    return render(request,'about.html')

def coursedetail(request,itemID):
    coursedt = Course.objects.get(pk=itemID)
    exam=coursedt.exam_set.get()
    return render (request,'coursedetail.html',{'course':coursedt,'exam':exam})

def exam(request,itemID):
    exam = Exam.objects.get(pk=itemID)
    quizs = exam.quiz_set.all()
    q={}
    for qz in quizs:
        q[qz]=qz.choice_set.all()
    return render(request,'exam.html',{'exam':exam,'quiz':quizs,'q':q})

def checkanswer(request):
    myDict=dict(request.POST.dict())
    Score=0
    TotalScore = 0
    for key,value in myDict.items():
        if(key!='csrfmiddlewaretoken'):
            TotalScore = TotalScore + 1
            if(value=='True'):
                Score=Score+1
    # answer = request.POST
    # if answer == True:

    return render(request,'chkAnswer.html',{'data':Score,'score':TotalScore})

def coursemath(request):
    allCourse=Course.objects.all

    return render(request,'coursemath.html',{'data':allCourse})

def coursesci(request):
    allCourse=Course.objects.all
    return render(request,'coursesci.html',{'data':allCourse})

def coursesocial(request):
    allCourse=Course.objects.all
    return render(request,'courseso.html',{'data':allCourse})

def thai(request):
    allCourse=Course.objects.all
    return render(request,'coursethai.html',{'data':allCourse})

def eng(request):
    allCourse=Course.objects.all
    return render(request,'courseeng.html',{'data':allCourse})
