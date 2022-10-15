from django.contrib import admin
from django.urls import path, include 
from restapi import urls as todo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restapi.urls')),
    #path('api-auth/', include('rest_framework.urls')),
]
