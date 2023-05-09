from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        county = request.POST['county']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)
        

        contact = Contact(car_id=car_id, phone_number=phone_number, email=email, message=message, county=county, first_name=first_name, last_name=last_name, user_id=user_id, car_title=car_title, customer_need=customer_need)


        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
                "New Car Inquiry",
                "You have a new inquiry for the car" + car_title + ". Please login to your admin account for more information.",
                "developer.dunnock@gmail.com",
                [admin_email],
                fail_silently=False,
            )

        contact.save()
        messages.success(request, 'Your request was submitted successfully, we will get back to you soon.')
        return redirect('/cars/'+car_id)
