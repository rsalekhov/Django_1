from django.http import HttpResponse
from django.shortcuts import render
import os
from datetime import datetime

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': '/',
        'Показать текущее время': '/current_time/',
        'Показать содержимое рабочей директории': '/workdir/'
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    workdir_contents = os.listdir('.')
    msg = f'Содержимое рабочей директории: {workdir_contents}'
    return HttpResponse(msg)

