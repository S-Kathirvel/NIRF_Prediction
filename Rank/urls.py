# your_app_name/urls.py
from django.urls import path
from .views import predict_view, home_view

urlpatterns = [
    path('predict/', predict_view, name='predict'),
    path('', home_view, name='home'),
    # Add any other paths as needed
]
