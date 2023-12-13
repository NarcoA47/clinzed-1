<<<<<<< HEAD

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
=======
from django.db import models

# Create your models here.
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
