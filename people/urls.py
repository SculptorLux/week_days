from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_fun),
    path('people_detail/', views.people_detail),
]