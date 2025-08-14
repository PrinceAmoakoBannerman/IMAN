from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Volunteer, Donation, Event
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    if request.method == 'POST':
        amount = int(request.POST.get('amount', 0)) * 100  # amount in dollars, convert to cents
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',  # <-- use USD for dollars
                    'product_data': {
                        'name': 'Donation',
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/donate-success/'),
            cancel_url=request.build_absolute_uri('/donate-cancel/'),
        )
        return JsonResponse({'id': session.id})

def home(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'accounts/index.html', {'upcoming_events': upcoming_events})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'accounts/signup.html')
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        login(request, user)
        messages.success(request, "You are signed in!")
        return redirect('profile')
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are signed in!")
            return redirect('home')
        else:
            error = "Invalid username or password."
            return render(request, 'accounts/login.html', {'error': error})
    return render(request, 'accounts/login.html')

def signout_view(request):
    logout(request)
    messages.success(request, "You have been signed out.")
    return redirect('login')

def donate_view(request):
    context = {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'accounts/donate.html', context)

def volunteer_view(request):
    context = {}
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if Volunteer.objects.filter(user=request.user).exists():
            context['volunteer_message'] = "Thank you for volunteering! You are already registered as a volunteer."
        else:
            Volunteer.objects.create(user=request.user, phone_number=phone_number)
            context['volunteer_message'] = "Thank you for signing up as a volunteer! Our team will contact you soon."
    return render(request, 'accounts/volunteer.html', context)

@login_required
def profile_view(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'accounts/profile.html', {'upcoming_events': upcoming_events})

def donate_success(request):
    return render(request, 'accounts/payment_success.html')

def donate_cancel(request):
    messages.info(request, "You cancelled the payment. No donation was made.")
    return redirect('donate')