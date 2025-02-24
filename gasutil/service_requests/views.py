from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ServiceRequest
from .forms import ServiceRequestForm

@method_decorator(login_required, name='dispatch')
class ServiceRequestCreateView(CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'service_requests/service_request_form.html'
    success_url = reverse_lazy('service_request_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ServiceRequestListView(ListView):
    model = ServiceRequest
    template_name = 'service_requests/service_request_list.html'
    context_object_name = 'requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(user=self.request.user).order_by('-created_at')

@method_decorator(login_required, name='dispatch')
class ServiceRequestDetailView(DetailView):
    model = ServiceRequest
    template_name = 'service_requests/service_request_detail.html'
