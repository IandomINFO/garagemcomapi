from django.contrib import admin

# Register your models here.
from .models import Marca, Categoria, Acessorio, Cor, Veiculo, Modelo

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Veiculo)
admin.site.register(Cor)
admin.site.register(Acessorio)
admin.site.register(Modelo)
