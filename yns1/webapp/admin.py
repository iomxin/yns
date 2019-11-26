from django.contrib import admin
from .models import Exam,Quiz,Choice,Subject,Course
# Register your models here.
admin.site.register(Exam)
admin.site.register(Quiz)
admin.site.register(Choice)
admin.site.register(Course)
admin.site.register(Subject)