from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse
from django.shortcuts import render


def get_rectangle_area(request, width: int, height: int):
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width: int):
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius: int):
    return render(request, 'geometry/circle.html')


def rectangle_redirect(request, width: int, height: int):
    redirect_url_rectangle = reverse('url_rectangle', args=(width, height))
    return HttpResponseRedirect(redirect_url_rectangle)


def square_redirect(request, width: int):
    redirect_url_square = reverse('url_square', args=(width,))
    return HttpResponseRedirect(redirect_url_square)


def circle_redirect(request, radius: int):
    redirect_url_circle = reverse('url_circle', args=(radius,))
    return HttpResponseRedirect(redirect_url_circle)