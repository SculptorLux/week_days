from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

dic_week_day = {'monday': 'Понедельник!',
                'tuesday': 'Вторник!',
                'wednesday': 'Среда!',
                'thursday': 'Четверг!',
                'friday': 'Пятница!',
                'saturday': 'Суббота!',
                'sunday': 'Воскресенье!'}


def get_info_about_day(request, day):
    description = dic_week_day.get(day, None)
    if description:
        return HttpResponse(dic_week_day[day])
    return HttpResponseNotFound(f'Нет такого дня в моей неделе {day}')


def get_info_by_number_of_day(request, number_of_day: int):
    if number_of_day <= 7:
        days_list = list(dic_week_day)
        day_x = days_list[number_of_day - 1]
        return HttpResponseRedirect(f'/todo_week/{day_x}')
    return HttpResponse(f'Неверный номер дня - {number_of_day}')