from django.urls import path, include
from . api import api
from . import views

urlpatterns = [
    path('api/', api.urls),
    path('listar/', views.listarTudo, name='listar'),
    # path('cadastrar/')
]