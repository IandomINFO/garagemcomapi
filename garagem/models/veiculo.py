from django.db import models
from garagem.models import  Modelo, Cor
from uploader.models import Image

class Veiculo(models.Model):
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    descricao = models.CharField(max_length=100)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")

    def __str__(self):
        return f"  {self.modelo} {self.marca} {self.ano} {self.cor}"
