# service_requests/forms.py
from django import forms
from .models import RequestStatus, ServiceRequest, Customer
from django.contrib.auth.models import User

class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['address', 'phone']

    def save(self, commit=True):
        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        customer = Customer(user=user, address=self.cleaned_data['address'], phone=self.cleaned_data['phone'])
        if commit:
            customer.save()
        return customer

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description']

class RequestStatusForm(forms.ModelForm):
    class Meta:
        model = RequestStatus
        fields = ['status']
