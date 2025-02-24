Testing Endpoints-



User Authentication
/accounts/register/ – Register a new user
/accounts/login/ – User login
/accounts/logout/ – Logout
/accounts/profile/ – View user profile


Customer Service Requests
/requests/new/ – Submit a service request
/requests/list/ – View all submitted requests
/requests/<int:pk>/ – View request details


Support Representative Dashboard
/support/ – View all service requests
/support/update/<int:pk>/ – Update the status of a service request


Admin Panel
/admin/ – Django admin panel for managing users and requests
