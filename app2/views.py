from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import student_form
from app.models import student

# Create your views here.
def home(request):
    return render(request, 'home.html')


def delete_record(request, x):
    d = student.objects.get(id=x)
    d.delete()
    return HttpResponseRedirect('/app/index')


def edit_record(request, x):
    d = student.objects.get(id=x)
    if request.method == "POST":
        form = student_form(request.POST, instance=d)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/app/index')
    else:
        form = student_form(instance = d)
    return render(request, "form.html", {"form": form})


def add_record(request):
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            # d = form.cleaned_data
            # q = student(name = d['name'], address = d['address'], marks = d['marks'])
            # q.save()
            return HttpResponseRedirect('/app/index')
    else:
        form = student_form()
    return render(request, 'form.html', {"form": form})