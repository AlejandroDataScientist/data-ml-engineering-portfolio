from django.shortcuts import render, get_object_or_404
from .models import Evento
from Apps.Formulario.forms import RegistroEventoForm 

def eventos_home(request):
    eventos = Evento.objects.all()
    return render(request, 'Eventos/eventos.html', {'eventos': eventos})

def registro_evento(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST, request.FILES)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.evento = evento
            participante.save()
            return render(request, 'Formulario/registro_exitoso.html', {'evento': evento})
    else:
        form = RegistroEventoForm()
    return render(request, 'Formulario/registro.html', {'form': form, 'evento': evento})
