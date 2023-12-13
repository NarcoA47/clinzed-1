<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from clean.views import homepage, signin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', signin, name='signin'),
    path('', homepage, name='homepage'),
    path('', include('clean.urls')),
]
=======

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings

from clean.views import homepage, signin

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signin/', signin, name='signin'),
    path('admin/', admin.site.urls),
    path('', include('clean.urls')),
] 
>>>>>>> cbc39ca5d3e5b9680ae161f0960b3a9c5bcaafd8
