from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ninja import ModelSchema, NinjaAPI, Schema
from . models import Editora
from pydantic import BaseModel
import json
apiE = NinjaAPI(urls_namespace='editora-api')

class EditorasSchema(ModelSchema):
    class Config:
        model = Editora
        model_fields = "__all__"
        
class EditoraUpdateSchema(BaseModel):
    nome: str
    fone: int

@apiE.get('listarTudo/')
def listarTudo(request):
    editoras = Editora.objects.all()
    response = [{'id':i.id,'nome': i.nome, 'fone': i.fone, } for i in editoras]
    return response


@apiE.post('cadastrarE/', response=EditorasSchema)
def cadastrarE(request, editora:EditorasSchema):
    editora_criada = editora.dict()
    editora = Editora(** editora_criada)
    editora.save()
    return editora


@apiE.delete('deletarE/{id}')
def deletarE(request, id: int):
    
    editora = Editora.objects.filter(id=id)
    count = editora.count()
    editora.delete()
    
    return {"message": f" {count} Editora deletada com sucesso"}


@apiE.put("editarE/{editora_id}")
def editarE(request, editora_id: int, payload: EditoraUpdateSchema):
    editora = get_object_or_404(Editora, id=editora_id)
    editora.nome = payload.nome
    editora.fone = payload.fone
    editora.save()
    
    return {"message": 'editora editada com sucesso'}
    
    
