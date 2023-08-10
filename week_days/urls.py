from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<int:number_of_day>/', views_week_days.get_info_by_number_of_day),
    path('<str:day>/', views_week_days.get_info_about_day, name='url_name_day'),
]