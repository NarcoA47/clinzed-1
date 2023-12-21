
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_start_date = models.DateTimeField()
    subscription_end_date = models.DateField()
    def __str__(self):
        return self.user.username



class Checkout(models.Model):
    name = models.CharField(max_length=255)
    area = models.CharField(max_length=255, choices=[('kabwata', 'matero'), ('chelstone', 'kalingalinga')])
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(default=None, null=True, blank=True)
    pickup_type = models.CharField(max_length=20, choices=[('one-time', 'One-time Pickup'), ('subscription', 'Subscription')])
    pickup_time = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

    
class Pickup(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    pickup_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)
