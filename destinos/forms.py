from django import forms
from .models import Destino


class DestinoForm(forms.ModelForm):

    class Meta:
        model = Destino
        fields = ['nombre', 'pais', 'precio', 'cupos', 'descripcion']

    def clean_precio(self):
        precio = self.cleaned_data['precio']

        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que 0.')

        return precio

    def clean_cupos(self):
        cupos = self.cleaned_data['cupos']

        if cupos < 0:
            raise forms.ValidationError('Los cupos no pueden ser negativos.')

        return cupos