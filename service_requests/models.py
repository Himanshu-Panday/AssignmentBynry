# service_requests/models.py
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('Install', 'Installation'),
        ('Repair', 'Repair'),
        ('Inquiry', 'Inquiry'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class RequestStatus(models.Model):
    request = models.OneToOneField(ServiceRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
