<<<<<<< HEAD:clinzed-1-main/clean/forms.py

from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name', 'area', 'pickup_type']
=======

from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name', 'area', 'pickup_type']
>>>>>>> 5d934d5 (Legcay dev):client/clean/forms.py
