<<<<<<< HEAD
from django.urls import path
from . import views
from .views import checkout

urlpatterns = [
=======
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
   path('', views.homepage, name="homepage"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
<<<<<<< HEAD
   path('checkout/', checkout, name='checkout'),
   
]
=======
   
   
  ]
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
