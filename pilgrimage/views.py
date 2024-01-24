# In pilgrimage/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Booking
from django.contrib.auth.views import LoginView

def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'pilgrimage/homepage_authenticated.html', {'user': request.user})
    return render(request, 'pilgrimage/homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('pilgrimage:homepage')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = UserCreationForm()
    return render(request, 'pilgrimage/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('pilgrimage:homepage')
        else:
            # Authentication failed
            try:
                existing_user = User.objects.get(username=username)
                messages.error(request, 'Login failed. Incorrect password for the given username.')
            except User.DoesNotExist:
                messages.error(request, 'Login failed. The provided username does not exist.')
    return render(request, 'pilgrimage/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('pilgrimage:homepage')

@login_required
def profile(request):
    return render(request, 'pilgrimage/profile.html')

def about(request):
    return render(request, 'pilgrimage/about.html')

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)  # Make sure you have the Booking model
    return render(request, 'pilgrimage/booking_history.html', {'bookings': bookings})


def book_ticket(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        date_of_visit = request.POST.get('date_of_visit')
        service = request.POST.get('service')

        # Create a new booking
        Booking.objects.create(
            user=request.user,
            name=name,
            email=email,
            date_of_visit=date_of_visit,
            service=service
        )

        messages.success(request, 'Ticket booked successfully!')
        return redirect('pilgrimage:booking_history')  # Redirect to booking history after booking

    return render(request, 'pilgrimage/book_ticket.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful. Thanks for visiting!')
    return redirect('pilgrimage:homepage')


class CustomLoginView(LoginView):
    template_name = 'pilgrimage/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Login successful. Welcome back!')
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Login failed. Please enter the correct username and password.')
        return response