from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name='url_rectangle'),
    path('square/<int:width>/', views.get_square_area, name='url_square'),
    path('circle/<int:radius>/', views.get_circle_area, name='url_circle'),
    path('get_rectangle_area/<int:width>/<int:height>/', views.rectangle_redirect),
    path('get_square_area/<int:width>/', views.square_redirect),
    path('get_circle_area/<int:radius>/', views.circle_redirect),
]