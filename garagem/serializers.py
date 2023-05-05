from rest_framework.serializers import ModelSerializer

from garagem.models import Cor, Marca, Categoria, Acessorio, Veiculo, Modelo


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"


class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"


class ModeloSerializer(ModelSerializer):
    class Meta:
        model = Modelo
        fields = "__all__"
