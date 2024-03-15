from django.db import models


class usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    
    def __str__(self):
        return self.nome