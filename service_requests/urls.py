# service_requests/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_customer, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_request, name='track_request'),
    path('manage/<int:request_id>/', views.manage_request, name='manage_request'),
]
