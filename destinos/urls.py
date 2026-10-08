from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('destinos/', views.lista_destinos, name='lista_destinos'),
    path('destinos/crear/', views.crear_destino, name='crear_destino'),
    path('destinos/editar/<int:id>/', views.editar_destino, name='editar_destino'),
    path('destinos/eliminar/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
]