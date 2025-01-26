from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.CharField(max_length=255)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)  # Indica se a notícia está ativa

    def __str__(self):
        return self.titulo
