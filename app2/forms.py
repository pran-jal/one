from multiprocessing import managers
from django import forms
from app.models import *

# class student_form(forms.Form):
#     name = forms.CharField(max_length=30)
#     address = forms.CharField(max_length=50)
#     marks = forms.IntegerField()
    
class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'