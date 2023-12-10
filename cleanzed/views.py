from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.utils.text import slugify

from .forms import CustomUserForm
from .models import UserAccount, UserManager
from store.forms import ListingForm

def Manager(request):
     
     form = ListingForm
     
     if request.method == 'POST':
          form = ListingForm(request.POST, request.FILES)
          
          if form.is_valid():
               title = request.POST.get('title')
               slug = slugify('title')
               listing = form.save(commit=False)
               listing.user = request.user
               listing.slug = slug
               listing.save()
               
               redirect ('homepage')
               
     return render(request, 'pages/admin/admin.html', {
          'form': form
     })


def account(request):
     return render(request, 'pages/tenants/account.html')

def favourite(request):
     return render(request, 'pages/tenants/favourite.html')
def invite(request):
     return render(request, 'pages/tenants/invite.html')

def profile(request):
     
     users = UserAccount.objects.all()
     
     return render(request, 'pages/tenants/profile.html', {
          'users': users,
     })

def signup(request):
    if request.method == 'POST':
         
         form = CustomUserForm(request.POST)
        
         if form.is_valid():
               user = form.save()
               login(request, user)
               
               messages.success(request, "Registration successful." )
               return redirect('account') 
          
    else:
         form = CustomUserForm()  
        
    return render(request, 'pages/signin.html', {
         'form': form
    })
    
def signin(request):
     if request.method == 'POST':
          
          form = AuthenticationForm(request.POST, data=request.POST)
          
          if form.is_valid():
               
               email = form.cleaned_data.get('email')
               password = form.cleaned_data.get('password')
               user = authenticate(email=email, password=password)
               
               if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {email}.")
                    return redirect(request, "pages/homepage")
               
          else:
               messages.error(request,"Invalid username or password.")
     else:
          form = AuthenticationForm()
               
     return render(request, 'pages/login.html', {
         'form': form
    })