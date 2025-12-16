#home/url.py
from django.urls import path
from .views import *

urlpatterns = [
    path('student_list/', student_list),
    path('student/<int:id>/', student_detail)
]


