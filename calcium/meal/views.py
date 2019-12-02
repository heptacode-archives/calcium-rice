from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from meal.models import Meal

def index(request):
    latest_meal_list = Meal.objects.all().order_by('-date')[:5]
    return render(request, 'index.html', {'latest_meal_list': latest_meal_list})

def detail(request):
    latest_meal_list = Meal.objects.all().order_by('-date')[:5]
    return render(request, 'detail.html', {'latest_meal_list': latest_meal_list})