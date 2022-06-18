from django.shortcuts import render
from .models import *

def home(request):

    students = Student.objects.all()

    return render(request,'home.html',{
        'students':students
    })

