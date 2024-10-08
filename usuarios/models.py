from django.db import models
from django.contrib.auth.models import User

class Estoque(models.Model):
    nome = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    
    # Relacionamento com o usuário, permite valores nulos e em branco
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.item} ({self.quantidade})'
