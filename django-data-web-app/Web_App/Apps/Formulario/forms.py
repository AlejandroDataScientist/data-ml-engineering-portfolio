from django import forms
from .models import RegistroEvento
import re
from django.utils.safestring import mark_safe


EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class RegistroEventoForm(forms.ModelForm):
    acepta_politicas = forms.BooleanField(
        label=mark_safe('He leído y acepto las <a href="/politicas/" target="_blank">políticas de privacidad</a>'),
        required=True
    )
    desea_recibir_noticias = forms.BooleanField(
        label='Deseo recibir noticias de próximos eventos',
        required=False
    )

    class Meta:
        model = RegistroEvento
        fields = ['nombre', 'correo', 'telefono', 'identificacion', 'logo', 'comentario', 'acepta_politicas', 'desea_recibir_noticias']
        exclude = ['evento']

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if len(telefono) < 10:
            raise forms.ValidationError("El teléfono debe tener al menos 10 dígitos.")
        return telefono

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if not re.match(EMAIL_REGEX, correo):
            raise forms.ValidationError("Por favor, introduce un correo válido.")
        return correo
