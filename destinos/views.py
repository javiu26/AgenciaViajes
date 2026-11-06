from django.shortcuts import render, redirect, get_object_or_404
from .models import Destino
from .forms import DestinoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import DestinoSerializer

@login_required
def inicio(request):
    return render(request, 'destinos/inicio.html')

@login_required
def lista_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'destinos/destinos.html', {'destinos': destinos})

@login_required
def crear_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinoForm()

    return render(request, 'destinos/crear_destino.html', {'form': form})

@login_required
def editar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)

    if request.method == 'POST':
        form = DestinoForm(request.POST, instance=destino)

        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinoForm(instance=destino)

    return render(request, 'destinos/editar_destino.html', {
        'form': form,
        'destino': destino
    })

@login_required
def eliminar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)

    if request.method == 'POST':
        destino.delete()
        return redirect('lista_destinos')

    return render(request, 'destinos/confirmar_eliminar.html', {
        'destino': destino
    })

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')

        else:
            return render(request, 'destinos/login.html', {
                'error': 'Usuario o contraseña incorrectos.'
            })

    return render(request, 'destinos/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

class DestinoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    permission_classes = [IsAuthenticated]


class DestinoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destino.objects.all()
    serializer_class = DestinoSerializer
    permission_classes = [IsAuthenticated]