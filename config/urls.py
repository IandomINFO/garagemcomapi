from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import (
    CategoriaViewSet,
    MarcaViewSet,
    AcessorioViewSet,
    ModeloViewSet,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"acessorios", AcessorioViewSet)
router.register(r"modelos", ModeloViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
