from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.index, name='index'),
    path('viewemployee/', views.employee, name='employee'),
 path('update-employee/<int:employee_id>/', views.update_employee_view, name='update-employee'),



]
