from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('destinos/', views.lista_destinos, name='lista_destinos'),
    path('destinos/crear/', views.crear_destino, name='crear_destino'),
    path('destinos/editar/<int:id>/', views.editar_destino, name='editar_destino'),
    path('destinos/eliminar/<int:id>/', views.eliminar_destino, name='eliminar_destino'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('api/destinos/', views.DestinoListCreateAPIView.as_view(), name='api_destinos'),
    path('api/destinos/<int:pk>/', views.DestinoDetailAPIView.as_view(), name='api_destino_detalle'),
    path('api/token/', obtain_auth_token, name='api_token'),
]