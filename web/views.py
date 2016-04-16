from django.shortcuts import render
from django.http import HttpResponse
from web.models import *


exams = {
    'мат': 'математика',
    'инф': 'информатика',
    'ино': 'иностранный',
    'общ': 'обществознание',
    'гео': 'география',
    'био': 'биология',
    'рус': 'русский язык',
    'ист': 'история',
    'физ': 'физика',
    'лит': 'литература',
    'твр': 'творческая работа',
    'хим': 'химия',
}


def index(request):
    return render(request, 'base.html', {'exams': exams})


def select(request):
    universities = list(University.objects.all())
    faculties = list(Faculty.objects.all())
    lines = list(Line.objects.all())
    return render(request, 'select.html', {'univ': universities, 'facu': faculties, 'line': lines})
