from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from service_requests.models import ServiceRequest

@staff_member_required
def support_dashboard(request):
    service_requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'support/support_dashboard.html', {'service_requests': service_requests})

@staff_member_required
def update_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get('status')
        if new_status in dict(ServiceRequest.STATUS_CHOICES).keys():
            service_request.status = new_status
            service_request.save()
            return redirect('support_dashboard')
    return render(request, 'support/update_status.html', {
        'service_request': service_request, 
        'status_choices': ServiceRequest.STATUS_CHOICES
    })
