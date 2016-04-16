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
    exams = list(Line.objects.raw('select exams, exam_mins from web_line left join '))
