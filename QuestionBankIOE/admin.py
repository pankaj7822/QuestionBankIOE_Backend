from django.contrib import admin
from .models import Course,CourseType,Department,ExamInformation,MarkingScheme,QuestionPaper
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)

models_ioe=[Course,CourseType,Department,ExamInformation,MarkingScheme,QuestionPaper]

for model in models_ioe:
    admin.site.register(model)