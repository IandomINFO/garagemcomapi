from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Marca, Acessorio, Modelo, Cor, Veiculo
from garagem.serializers import (
    CategoriaSerializer,
    MarcaSerializer,
    AcessorioSerializer,
    ModeloSerializer,
)


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer


class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
