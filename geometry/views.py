import math
from django.http import HttpResponse
from math import pi


# Create your views here.


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника {width} * {height} = {width * height}")


def get_square_area(request, width: int):
    return HttpResponse(f"Площадь квадрата со стороной {width} = {width ** 2}")


def get_circle_area(request, radius: int):
    return HttpResponse(f"Площадь круга с радиусом {radius} = {(radius * pi) ** 2}")
