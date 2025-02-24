from django.urls import path
from .views import ServiceRequestCreateView, ServiceRequestListView, ServiceRequestDetailView

urlpatterns = [
    path('new/', ServiceRequestCreateView.as_view(), name='service_request_create'),
    path('list/', ServiceRequestListView.as_view(), name='service_request_list'),
    path('<int:pk>/', ServiceRequestDetailView.as_view(), name='service_request_detail'),
]
