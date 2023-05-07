from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.

def home(request):
    teams = Team.objects.all()
    cars = Car.objects.order_by('-created_date')
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    model_search = Car.objects.values_list('model', flat=True).distinct() 
    county_search = Car.objects.values_list('county', flat=True).distinct() 
    year_search = Car.objects.values_list('year', flat=True).distinct() 
    body_type_search = Car.objects.values_list('body_type', flat=True).distinct() 
    data = {
        'teams': teams,
        'cars': cars,
        'featured_cars': featured_cars,
        'model_search': model_search,
        'county_search': county_search,
        'year_search': year_search,
        'body_type_search': body_type_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
    }
    return render(request, 'pages/about.html',data)


def services(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/services.html',data)


def contact(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/contact.html',data)

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')