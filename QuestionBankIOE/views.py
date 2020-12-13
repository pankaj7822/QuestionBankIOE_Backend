from .models import QuestionPaper,Course
from django.http import JsonResponse
import json

def getpaper(request):
    papers = QuestionPaper.objects.all()
    paper_list=[]
    for paper in papers:
        dic={"course_code":paper.course.id,"course_title":paper.course.title,"semester":paper.course.semester,"department":paper.course.depart_code.name,"program":paper.course.program,"course_type":paper.course.type_code.type_name,"year":paper.exam.year,"type":paper.exam.type,"link":paper.paper_link}
        paper_list.append(dic)
    return JsonResponse({"paper_list":paper_list})

def getcourses(request):
    courses=Course.objects.all()
    courselist=[]
    courselist.append("")
    for course in courses:
        courselist.append(course.title)
    return JsonResponse({"course_list":courselist})