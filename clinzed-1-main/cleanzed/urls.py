from django.contrib import admin
from django.urls import path, include
from clean.views import homepage, signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', signin, name='signin'),
    path('', homepage, name='homepage'),
    path('', include('clean.urls')),
]
