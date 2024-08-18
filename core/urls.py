from django.contrib import admin
from django.urls import path, include
from editora.api import apiE


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', include('cadastro.urls')),
    path('editora/', include('editora.urls')),
]
