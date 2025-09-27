from django.shortcuts import render
from .models import Evento, Participantes
from .form import EventoForm, ParticipantesForm

def index(request):
    eventos = Evento.objects.all()
    participante = Participantes.objects.all()
    return render(request, 'index.html', {'eventos': eventos, 'participante': participante})

def base(request):
    return render(request, 'base.html')

def footer(request):
    return render(request, 'footer.html')

def formulario_base(request):
    return render(request, 'formulario_base.html')

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

def registro_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registro_exitoso.html')
    else:
        form = EventoForm()
    return render(request, 'registro_evento.html', {'form': form})

def registro_participantes(request):
    if request.method == 'POST':
        participante_form = ParticipantesForm(request.POST)
        if participante_form.is_valid():
            participante_form.save()
            return render(request, 'registro_exitoso.html')
    else:
        participante_form = ParticipantesForm()
    return render(request, 'registro_participantes.html', {'form': participante_form})