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


def get_info_by_number_of_day(request, number_of_day: int):
    if number_of_day <=7:
        return HttpResponse(f'Сегодня {number_of_day} день недели')
    return HttpResponse(f'Неверный номер дня - {number_of_day}')