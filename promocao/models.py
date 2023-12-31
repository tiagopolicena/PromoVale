from django.db import models

class Promocao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    mercado = models.ForeignKey("mercado.Mercado", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='promocoes_images/')
    image = models.ImageField(upload_to='logo_images/')
    
    

    def __str__(self):
        return self.titulo

