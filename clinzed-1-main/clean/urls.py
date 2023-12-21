from django.urls import path
from . import views
from .views import checkout

urlpatterns = [
   path('', views.homepage, name="homepage"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('checkout/', checkout, name='checkout'),
   
]
