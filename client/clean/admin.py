from django.contrib import admin

from .models import UserProfile, Checkout

admin.site.register(UserProfile),
admin.site.register(Checkout)

