from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=30)
    senha = models.CharField(max_length=16)
    pontos = models.DecimalField(max_digits=16)
    # email = models.CharField(max_length=30)


class Nota(models.Model):
    codigo = models.CharField(max_length=20)
    num_produtos = models.DecimalField(max_digits=5)


class Produto(models.Model):
    descricao = models.TextField
    
# Pelo amor de Deus me deem sugestões ae tem que fazer função até pra ficar bonitinho falem o que dá pra fazer que eu vou fazendo
# aqui eu simplesmente não tô conseguindo pensar direito aqui ok vlw
