
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static 
from django.conf import settings

from clean.views import homepage, signin

urlpatterns = [
    path('', homepage, name='homepage'),
    path('signin/', signin, name='signin'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
