from django.urls import path, include
from . api import apiE
from . import views


urlpatterns = [
    path('apiE/', apiE.urls, name='apiE'),
    path('listarE/', views.listarTudoE, name='listarE'),
    path('cadastrarE/', views.cadastrarE, name='cadastrarE'),
    path('deletarE/<int:id>', views.deletarE, name='deletarE'),
    path('telaEditar/<int:id>', views.tela_editar, name='Tela_Editar'),
    path('editarE/<int:id>', views.editarE, name='editarE'),
]