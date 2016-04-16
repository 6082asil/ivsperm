from django.contrib import admin
from web.models import *


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('verbose', 'city')


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('verbose', 'university')


@admin.register(Line)
class LineAdmin(admin.ModelAdmin):
    list_display = ('verbose', 'faculty')
