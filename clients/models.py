from django.db import models

class Client(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    cep = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
