from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import (
    AcessorioViewSet,
    CategoriaViewSet,
    CorViewSet,
    MarcaViewSet,
    ModeloViewSet,
    VeiculoViewSet,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"modelos", ModeloViewSet)
router.register(r"cores", CorViewSet)
router.register(r"veiculos", VeiculoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
