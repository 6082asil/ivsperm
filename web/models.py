from django.db import models

class University(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=256,
        default='',
        blank=True,
        unique=True,
        verbose_name='Код в базе',
    )
    verbose = models.CharField(
        max_length=256,
        default='',
        blank=True,
        unique=True,
        verbose_name='Полное название на русском',
    )
    city = models.CharField(
        max_length=256,
        default='',
        blank=True,
        unique=False,
        verbose_name='Город',
    )
    faculties = models.CharField(
        max_length=65536,
        default='',
        blank=True,
        unique=False,
        verbose_name='Коды факультетов',
    )
    website = models.URLField(
        max_length=256,
        default='',
        blank=True,
        unique=False,
        verbose_name='Веб-сайт',
    )

    def __str__(self):
        return self.verbose


class Faculty(models.Model):
    code = models.CharField(
        max_length=256,
        default='',
        blank=True,
        unique=False,
        verbose_name='Код факультета',
    )
    verbose = models.CharField(
        max_length=256,
        default='',
        blank=True,
        unique=False,
        verbose_name='Название факультета',
    )
    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE,
        verbose_name='Университет',
    )
    lines = models.CharField(
        max_length=65536,
        default='',
        blank=True,
        unique=False,
        verbose_name='Коды специальностей',
    )


    def __str__(self):
        return self.verbose


class Line(models.Model):
    code = models.CharField(
        primary_key=True,
        default='',
        max_length=256,
        blank=True,
        unique=False,
        verbose_name='Код специальности',
    )
    verbose = models.CharField(
        default='',
        max_length=256,
        blank=True,
        unique=False,
        verbose_name='Название специальности',
    )
    faculty = models.ForeignKey(
        'Faculty',
        on_delete=models.CASCADE,
        verbose_name='Факультет',
    )
    exams = models.CharField(
        default='',
        max_length=256,
        blank=True,
        unique=False,
    )
    exam_mins = models.CharField(
        default='',
        max_length=256,
        blank=True,
        unique=False,
    )
    budget = models.IntegerField(
        default=0,
        blank=True,
        unique=False,
    )
    commercial = models.IntegerField(
        default=0,
        blank=True,
        unique=False,
    )
