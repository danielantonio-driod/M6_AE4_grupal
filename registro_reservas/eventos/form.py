from django import forms
from .models import Evento, Participantes
from django.utils import timezone
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion', 'descripcion']
        widgets = {
            'fecha': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'descripcion': forms.Textarea(attrs={'rows': 4})
        }
        labels = {
            'nombre': 'Nombre del Evento',
        }
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha < timezone.now().date():
            raise forms.ValidationError("La fecha no puede ser en el pasado.")
        return fecha
class ParticipantesForm(forms.ModelForm):
    class Meta:
        model = Participantes
        fields = ['evento', 'nombre', 'correo', 'telefono']
        labels = {
            'nombre': 'Nombre del Participante',
            'correo': 'Correo Electrónico',
        }
        evento = forms.ModelChoiceField(queryset=Evento.objects.all(), empty_label="Seleccione un evento")
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if Participantes.objects.filter(correo=correo).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return correo