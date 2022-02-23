"""petstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#These 2 imports are used in Development ONLY to 'serve' media and static files.
#By default, Django includes the app "django.contrib.staticfiles", which serves your static files from each app (no need for these imports), but
#if you wanted to 'serve' media files (uploaded images/files by users), you need to use these imports, and bottom code (media part only).
#If we where to DELETE "django.contrib.staticfiles" app in settings.py, we NEED these 2 imports in order to serve media & static files.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-edu-9005!/', admin.site.urls),
    path('', include('simbapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#When deploying to Heroku:

# [

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




#In Development:

#We add this if we want to serve media/static in development.
#If 'django.contrib.staticfiles' app is NOT deleted in settings.py, then we only need to add the 'media' part.
#If 'django.contrib.staticfiles' app IS deleted, we need both, media and static code shown below.
# if settings.DEBUG: 
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
