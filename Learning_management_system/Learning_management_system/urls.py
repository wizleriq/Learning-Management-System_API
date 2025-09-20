"""
URL configuration for Learning_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Learning Management API Dveloped By Wisdom Darlington Ndata")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    # path("auth/", include("accounts.urls")),

    # JWT auth
    path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-create'),
    
    path('auth/', include('djoser.urls')), # user management
    path('auth/', include('djoser.urls.authtoken')), # If using token authentication
    path('auth/', include('djoser.urls.jwt')) # JWT-specific endpoints
]

# urlpatterns = [
#     path('', home),
#     path('admin/', admin.site.urls),

#     # Djoser authentication
#     path('auth/', include('djoser.urls')),  # default user management (register, etc.)
#     path('auth/', include('djoser.urls.authtoken')),  # Token authentication
#     path('auth/', include('djoser.urls.jwt')),  # JWT authentication

#     # JWT endpoints (explicit if you want direct access)
#     path('auth/jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
#     path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
# ]

