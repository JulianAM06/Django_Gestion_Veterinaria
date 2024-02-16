from django.db import models


class Cliente(models.Model):

    idCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    cedula = models.CharField(max_length=50, blank=False, null=False, default = 123456789)
    email = models.EmailField(blank=False, null=False)
    telefono = models.CharField(max_length=10, blank=False, null=False)
    ciudad = models.CharField(max_length=50, blank=False, null=False, default = 'Medellin')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'

    def __str__(self):
        return self.nombre + " " + self.apellido
    

class Veterinario(models.Model):

    idVeterinario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    cedula = models.CharField(max_length=50, blank=False, null=False, default = 123456789)
    especialidad = models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        db_table = 'Veterinarios'

    def __str__(self):
        return self.nombre + " - " + self.especialidad
    
    
class Mascota(models.Model):

    idMascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False, default=0)
    raza = models.CharField(max_length=50, blank=False, null=False)
    peso = models.FloatField(blank=False, null=False)
    foto = models.ImageField(upload_to='mascotas', blank=False, null=False)
    descripcion = models.TextField(max_length=500, blank=False, null=False, default = 'Ingresa descripcion mascota')
    fkCliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        db_table = 'Mascotas'

    def __str__(self):
        return self.nombre + " - " + str(self.fkCliente)
    

class Tratamiento(models.Model):

    idTratamiento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    fecha = models.DateField(blank=False, null=True)
    precio = models.IntegerField(blank=False, null=True, default=0)
    descripcion = models.TextField(max_length=500, default="Ingresa descripcion del Tratamiento realizado")
    fkMascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, null=True)
    fkVeterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'
        db_table = 'Tratamientos'

    def __str__(self):
        return self.nombre + " - " + str(self.fecha)
    
    
class mascotasAdopciones(models.Model):

    idMascotaAdopcion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    especies = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato')
    ]
    especie = models.CharField(max_length = 5, choices = especies, default = 'Perro')
    raza = models.CharField(max_length=50, blank=False, null=False)
    edad = models.IntegerField(blank=False, null=False, default=0)
    sexos = [
        ('Hembra', 'Hembra'),
        ('Macho', 'Macho')
    ]
    sexo = models.CharField(max_length = 6, choices = sexos, default = 'Hembra')
    castrado = models.BooleanField()
    descripcion = models.TextField(max_length=500)
    foto = models.ImageField(upload_to='adopciones', default="foto")
    

    class Meta:
        verbose_name = 'MascotaAdopcion'
        verbose_name_plural = 'MascotasAdopciones'
        db_table = 'MascotasAdopciones'

    def __str__(self):
        return self.nombre + " - " + self.raza + " - " + self.especie + " - " + self.sexo



    

