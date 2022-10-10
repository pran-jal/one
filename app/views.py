from urllib import request
from django.shortcuts import render
from django.http import *
from .models import *
from app2.forms import *

def index(request):
    # obj = student(name = "harsh", address = "delhi", marks = "70")
    # obj.save()
    stu = student.objects.all()
    cd = {'stu':stu}
    return render(request, 'index.html', cd)

def show(request, id):
    stu = student.objects.get(id=id)
    cd = {'stu': stu}
    return render(request, 'show.html', cd)
