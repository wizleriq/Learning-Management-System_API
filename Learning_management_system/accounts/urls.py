from django.urls import path
from .views import RegisterListView

urlpatterns = [
    path('register/', RegisterListView.as_view(), name='register')
]
