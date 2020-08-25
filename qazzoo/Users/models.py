from djongo import models
from django.contrib.auth.models import User

class profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    place = models.CharField(max_length=100)
    desc = models.TextField(max_length=2000)
    
    
    
    def __str__(self):
        return f'{self.user.username} Profile'