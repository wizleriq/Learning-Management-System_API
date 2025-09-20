from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

# To register new users even when I have djoser installed (do this if you dont have djoser installed )
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        def create(self, validated_data):
            user = User.objects.create_user(
                username =  validated_data['username'],
                email = validated_data.get('email'),
                password = validated_data['password']
            )
            return user 
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = []

# To view list of registerd users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
