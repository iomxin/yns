from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField(max_length = 10000)
    Subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'static/image/',null = True,blank=True)
    def __str__(self):
        return self.name
    
class Exam(models.Model):
    name = models.CharField (max_length = 50)
    detail = models.TextField(max_length = 200,blank = True)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Quiz(models.Model):
    name = models.CharField(max_length = 50)
    exam = models.ForeignKey('Exam',on_delete=models.CASCADE)
    img = models.FileField(upload_to='static/image/',null = True,blank=True)
    def __str__(self):
        return self.name
    
class Choice(models.Model):
    name = models.CharField(max_length = 50)
    quiz = models.ForeignKey('Quiz',on_delete=models.CASCADE,null=True)
    img = models.FileField(upload_to = 'static/image/',null = True,blank=True)
    corrected = models.BooleanField(default = False)
    def __str__(self):
        return self.name
    