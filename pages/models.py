from django.db import models

class Page(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    imagem_box = models.ImageField()  #upload_to ='uploads/'
    data_criacao = models.DateTimeField("Data de Criação", auto_now_add=True)
    data_atualizacao = models.DateTimeField("Data de Atualização", auto_now=True)
    
    def __str__(self):
        return self.titulo
    
