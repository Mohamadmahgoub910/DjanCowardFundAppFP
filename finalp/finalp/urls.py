from os import stat
from django.contrib import admin
from django.urls import path, include
from projects.views import projects
from projects import views
from users import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('profiles/', include('users.urls')),
    
]
# get images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
