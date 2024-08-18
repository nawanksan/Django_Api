from ninja import ModelSchema, NinjaAPI, Schema
from . models import Livro
import json
api = NinjaAPI()

class LivrosSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = "__all__"


@api.get('listarTudo/')
def listarTudo(request):
    livro = Livro.objects.all()
    response = [{'id':i.id,'name': i.name, 'descricao': i.descricao, 'autor': i.autor, } for i in livro]
    return response



@api.get('listar/{id}')
def listar(request, id):
    livro = Livro.objects.filter(id=id)
    response = [{'id':i.id, 'name': i.name, 'descricao': i.descricao, 'autor': i.autor } for i in livro]
    return response



@api.post('cadastrarLivro/')
def cadastrarLivro(request, livro:LivrosSchema):
    l1 = livro.dict()
    livro = Livro(** l1)
    livro.save()
    return livro


# @api.delete('deletarLivro/{id}')
# def deletarLivro(request, id):
#     Livro.objects.filter(id=id).delete()
#     Livro.save()
#     return {"message": "Livro deletado com sucesso"}