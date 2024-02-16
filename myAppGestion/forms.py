from django import forms
from .models import Mascota, Cliente, Tratamiento, mascotasAdopciones


class FormularioMascota(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'edad', 'raza', 'peso', 'foto', 'descripcion', 'fkCliente']

class FormularioCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre','apellido','cedula','email', 'telefono', 'ciudad']

class FormularioTratamiento(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['nombre','fecha','precio','descripcion','fkMascota', 'fkVeterinario']

class FormularioMascotaAdopcion(forms.ModelForm):
    class Meta:
        model = mascotasAdopciones
        fields = ['nombre','especie','raza','edad','sexo','castrado','foto','descripcion']
        