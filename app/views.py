from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Exam


def index(request):
    exams = Exam.objects.all()
    context = {
        'exams': exams,
    }
    return render(request, 'app/index.html', context)
