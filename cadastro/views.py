from django.shortcuts import render
import requests

def listarTudo(request):
    response = requests.get('http://127.0.0.1:8000/cadastro/api/listarTudo/')
    livros =  response.json()
    return render(request, 'home.html', {'livros': livros})