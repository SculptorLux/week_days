from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<day>/', views_week_days.get_info_about_day),
]