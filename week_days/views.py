from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def get_info_about_day(request, day):
    if day == 'monday':
        return HttpResponse('На понедельник нет планов')
    elif day == 'tuesday':
        return HttpResponse('Во вторник учим python')
    else:
        return HttpResponseNotFound('Прости, про твой день ничего не знаю')