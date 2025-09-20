from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, name='user')
    email = models.EmailField(name='email')
    # password = models.CharField(max_length=50, name='password')
    bio = models.TextField(max_length=500, blank=True, name='bio')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, name='profile_picture')
    created_at = models.DateTimeField(auto_now_add=True, name='crated_at')
    
    def __str__(self):
        return self.user.username
