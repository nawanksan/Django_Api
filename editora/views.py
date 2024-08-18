from django.shortcuts import get_object_or_404, render, redirect
from . models import Editora
import requests

def listarTudoE(request):
    response = requests.get('http://127.0.0.1:8000/editora/apiE/listarTudo/')
    editora =  response.json()
    return render(request, 'listar.html', {'editoras': editora})



def cadastrarE(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        fone =  request.POST.get('fone')
        
        data = {
            'nome': nome,
            'fone': fone,
        }
        
        requests.post('http://127.0.0.1:8000/editora/apiE/cadastrarE/', json=data)
        return redirect('listarE')
    else:
        return render(request, 'cadastrarE.html')
    
    
    
def deletarE(request, id):
        # data = {
        #     'nome': nome
        # }
        
        # url = f'http://127.0.0.1:8000/editora/apiE/deletarE/{nome}'
        
        requests.delete(f'http://127.0.0.1:8000/editora/apiE/deletarE/{id}')
        
        return redirect('listarE')
    

def tela_editar(request, id:int):
    response = requests.get('http://127.0.0.1:8000/editora/apiE/listarTudo/')
    editora = response.json()
    return render(request, 'editar.html', {'editora': editora})
    

def editarE(request, id:int):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        fone =  request.POST.get('fone')
        
        data = {
            'nome': nome,
            'fone': fone,
        }
        
        requests.put(f'http://127.0.0.1:8000/editora/apiE/editarE/{id}', json=data)
        return redirect('listarE')
    else:
        return render(request, 'editar.html')