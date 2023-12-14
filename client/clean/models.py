from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class Checkout(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    pickup_type = models.CharField(max_length=20, choices=[('one-time', 'One-time Pickup'), ('subscription', 'Subscription')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name