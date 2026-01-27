from django.shortcuts import render, get_object_or_404
from Apps.Eventos.models import Evento
from .forms import RegistroEventoForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/usuarios/login/')
def registrar_evento(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST, request.FILES)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.evento = evento
            participante.save()
            return render(request, 'Formulario/gracias.html', {'evento': evento})
    else:
        form = RegistroEventoForm()
    return render(request, 'Formulario/registro.html', {'form': form, 'evento': evento})
