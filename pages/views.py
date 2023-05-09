from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']


        email_subject = 'You have a new message from Used Cars Liberia website regarding' + subject 
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
                email_subject,
                message_body,
                "developer.dunnock@gmail.com",
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you soon.')
        return redirect('contact')
    
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/contact.html',data)