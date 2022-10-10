from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    re_path('delete_record/(\d+)/', delete_record, name='delete'),
    re_path('edit_record/(\d+)/', edit_record, name='edit'),
    path('add/', add_record, name='add'),

]
