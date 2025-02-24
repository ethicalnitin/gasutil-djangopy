from django.urls import path
from .views import support_dashboard, update_request_status

urlpatterns = [
    path('', support_dashboard, name='support_dashboard'),
    path('update/<int:pk>/', update_request_status, name='update_request_status'),
]
