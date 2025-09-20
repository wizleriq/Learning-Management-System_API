from django.shortcuts import render,
from .serializer import RegisterSerializer, ProfileSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import generics, filters

# Create your views here.
class RegisterListView(generics.ListAPIView):
    queryset = User.object.all()
    serializer_class = RegisterSerializer
    permission_class = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfileListCreateAPI(generics.ListCreateAPIView):
    