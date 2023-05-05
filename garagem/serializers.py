from rest_framework.serializers import ModelSerializer

from garagem.models import Cor, Marca, Categoria, Acessorio, Veiculo


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
