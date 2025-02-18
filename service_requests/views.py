from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import ServiceRequestForm, RequestStatusForm, CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def register_customer(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # ✅ Correct usage
            return redirect('track_request')  # Redirect after successful login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')
# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

def submit_request(request):
    if request.method == "POST":
        customer = get_object_or_404(Customer, user=request.user)  # Get the related Customer instance
        service_request = ServiceRequest(
            customer=customer,  # Assign Customer instance instead of User
            request_type=request.POST.get("request_type"),
            description=request.POST.get("description"),
        )
        service_request.save()
        return redirect("track_request")  
    form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

@login_required
def track_request(request):
    customer_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'track_request.html', {'requests': customer_requests})

@login_required
def manage_request(request, request_id):
    request_obj = ServiceRequest.objects.get(id=request_id)
    if request.method == 'POST':
        form = RequestStatusForm(request.POST, instance=request_obj)
        if form.is_valid():
            form.save()
            return redirect('track_request')
    else:
        form = RequestStatusForm(instance=request_obj)
    return render(request, 'manage_request.html', {'form': form, 'request': request_obj})
