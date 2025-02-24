# gasutil/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# A simple view to show something at the root URL
def home_view(request):
    return HttpResponse("Welcome to the Gas Utility Service!")

urlpatterns = [
    path('', home_view, name='home'),           # <-- Add this line for the root path
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('requests/', include('service_requests.urls')),
    path('support/', include('support.urls')),
]
