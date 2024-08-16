from django.db import models

class Livro(models.Model):
    name = models.CharField(max_length=100)
    descricao = models.TextField()
    autor = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.name