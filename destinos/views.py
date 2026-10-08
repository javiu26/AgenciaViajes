from django.shortcuts import render, redirect, get_object_or_404
from .models import Destino
from .forms import DestinoForm


def inicio(request):
    return render(request, 'destinos/inicio.html')


def lista_destinos(request):
    destinos = Destino.objects.all()
    return render(request, 'destinos/destinos.html', {'destinos': destinos})


def crear_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_destinos')
    else:
        form = DestinoForm()

    return render(request, 'destinos/crear_destino.html', {'form': form})


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


def eliminar_destino(request, id):
    destino = get_object_or_404(Destino, id=id)

    if request.method == 'POST':
        destino.delete()
        return redirect('lista_destinos')

    return render(request, 'destinos/confirmar_eliminar.html', {
        'destino': destino
    })