from django.shortcuts import render
from django.http import HttpResponse


exams = {
    'мат': 'математика',
    'инф': 'информатика',
    'ино': 'иностранный',
    'общ': 'обществознание',
    'гео': 'география',
    'био': 'биология',
    'рус': 'русский язык',
    'ист': 'история',
}


def index(request):
    return render(request, 'base.html', {'exams': exams})
