
from django import forms
from .models import Pickup

class CheckoutForm(forms.Form):
    name = forms.CharField(label='Name')
    address = forms.ChoiceField(
        label='address',
        choices=[
            ('Kabwata', 'Matero'),
            ('kalingalinga', 'chelstone'),
            
        ]
    )
    phone_number = forms.CharField(label='Phone Number')
    email = forms.EmailField(label='Email')
    
class PickupForm(forms.ModelForm):
    class Meta:
        model = Pickup
        fields = ['pickup_time']