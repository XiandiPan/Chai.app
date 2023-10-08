from django.shortcuts import render, get_object_or_404
from chai_schedule.models import Employee

# Create your views here.
def home_django(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})


