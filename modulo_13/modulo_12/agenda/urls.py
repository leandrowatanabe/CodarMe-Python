from django.urls import path
from agenda.views import listar_eventos, exibir_evento, participar_evento, listar_categorias, exibir_categoria

urlpatterns=[
    path("eventos/", listar_eventos, name="listar_eventos"),
    path("", listar_eventos, name="listar_eventos_raiz"),
    path("eventos/<int:id>", exibir_evento, name="exibir_evento"),
    path("categorias/", listar_categorias, name="listar_categorias"),
    path("categorias/<int:id>", exibir_categoria, name="exibir_categoria"),
    path("participar/", participar_evento, name="participar_evento")
]