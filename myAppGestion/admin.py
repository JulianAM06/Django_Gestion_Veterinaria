from django.contrib import admin
from .models import Cliente, Veterinario, Tratamiento, Mascota, mascotasAdopciones

class AdminCliente(admin.ModelAdmin):
    search_fields = ('nombre', 'idCliente', 'apellido',)
    list_filter = ('ciudad',)

admin.site.register(Cliente, AdminCliente)


class AdminVeterinario(admin.ModelAdmin):
    search_fields = ('nombre', 'especialidad', 'idVeterinario',)
    list_filter = ('especialidad',)

admin.site.register(Veterinario, AdminVeterinario)


class AdminTratamiento(admin.ModelAdmin):
    search_fields = ('nombre', 'idTratamiento',)
    list_filter = ('nombre',)

admin.site.register(Tratamiento, AdminTratamiento)


class AdminMascota(admin.ModelAdmin):
    search_fields = ('nombre', 'idMascota',)
    list_filter = ('raza',)

admin.site.register(Mascota, AdminMascota)


class AdminMascotaAdopciones(admin.ModelAdmin):
    search_fields = ('nombre', 'idMascotaAdopcion',)
    list_filter = ('raza',)

admin.site.register(mascotasAdopciones, AdminMascotaAdopciones)