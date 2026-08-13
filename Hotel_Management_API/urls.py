"""
URL configuration for Hotel_Management_API project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rooms.urls')),
    path('api/', include('Hotel.urls')),
    path('api/auth/', include('apps.urls')),
]