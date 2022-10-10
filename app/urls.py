from .views import *
from django.urls import path, re_path

urlpatterns = [
    path('index/', index, name='index'),
    re_path('show/(\d+)/', show, name='show')
    # re_path('delete_record/(\d+)/', delete_record, name='delete'),
]
