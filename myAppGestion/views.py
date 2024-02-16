from django.shortcuts import render, redirect
from .forms import FormularioMascota, FormularioCliente, FormularioTratamiento, FormularioMascotaAdopcion
from .models import Mascota, Cliente, Tratamiento, mascotasAdopciones
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q



def index(request):
    return render (request, 'index.html')

@login_required
def registrarMascota(request):

    context = {}

    if request.method == 'POST':

        form = FormularioMascota(request.POST, request.FILES)

        if form.is_valid():

            id = form.cleaned_data.get('idMascota')
            nom = form.cleaned_data.get('nombre')
            ed = form.cleaned_data.get('edad')
            raz = form.cleaned_data.get('raza')
            pes = form.cleaned_data.get('peso')
            fot = form.cleaned_data.get('foto')
            des = form.cleaned_data.get('descripcion')
            fkCl = form.cleaned_data.get('fkCliente')

            mascota = Mascota.objects.create(
                idMascota = id,
                nombre = nom,
                edad = ed,
                raza = raz,
                peso = pes,
                foto = fot,
                descripcion = des,
                fkCliente = fkCl,
            )

            mascota.save()
            form = FormularioMascota()
            
            return redirect('mostrarMascota/')

    else:

        form = FormularioMascota()
        

    context['form'] = form
    
    return render(request, 'registrarMascota.html', context)


def mostrarMascota (request):

    queryset = request.GET.get("buscar")

    mascotas = Mascota.objects.all()

    if queryset:
        
        mascotas = Mascota.objects.filter(
            
            Q(nombre__icontains = queryset) |
            Q(fkCliente__idCliente__icontains = queryset)
            
        ).distinct()

    

    return render(request, 'mostrarMascota.html', {'mascotas': mascotas})


@login_required
def registrarCliente(request):

    context = {}

    if request.method == 'POST':

        form = FormularioCliente(request.POST)

        if form.is_valid():

            id = form.cleaned_data.get('idCliente')
            nom = form.cleaned_data.get('nombre')
            ap = form.cleaned_data.get('apellido')
            ced = form.cleaned_data.get('cedula')
            em = form.cleaned_data.get('email')
            tel = form.cleaned_data.get('telefono')
            ciu = form.cleaned_data.get('ciudad')

            cliente = Cliente.objects.create(
                idCliente = id,
                nombre = nom,
                apellido = ap,
                cedula = ced,
                email = em,
                telefono = tel,
                ciudad = ciu,
            )

            cliente.save()
            form = FormularioCliente()
            return redirect('mostrarCliente/')
        

    else:

        form = FormularioCliente()

    context['form'] = form

    return render(request, 'registrarCliente.html', context)

def mostrarCliente(request):

    queryset = request.GET.get("buscar")

    clientes = Cliente.objects.all()

    if queryset:
        
        clientes = Cliente.objects.filter(
            
            Q(nombre__icontains = queryset) |
            Q(cedula__icontains = queryset)
            
        ).distinct()

    return render(request, 'mostrarCliente.html', {'clientes': clientes})


@login_required
def registrarTratamiento(request):

    context = {}

    if request.method == 'POST':

        form = FormularioTratamiento(request.POST)

        if form.is_valid():

            id = form.cleaned_data.get('idTratamiento')
            nom = form.cleaned_data.get('nombre')
            fe = form.cleaned_data.get('fecha')
            pre = form.cleaned_data.get('precio')
            des = form.cleaned_data.get('descripcion')
            fkm = form.cleaned_data.get('fkMascota')
            fkv = form.cleaned_data.get('fkVeterinario')

            tratamiento = Tratamiento.objects.create(
                idTratamiento = id,
                nombre = nom,
                fecha = fe,
                precio = pre,
                descripcion = des,
                fkMascota = fkm,
                fkVeterinario = fkv,
            )

            tratamiento.save()
            form = FormularioTratamiento()

            return redirect('mostrarTratamiento/')
        

    else:

        form = FormularioTratamiento()

    context['form'] = form

    return render(request, 'registrarTratamiento.html', context)

def mostrarTratamiento(request):

    busqueda = request.GET.get("buscar")

    tratamientos = Tratamiento.objects.all()

    if busqueda:
        
        tratamientos = Tratamiento.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(fecha__icontains = busqueda) |
            Q(idTratamiento__icontains = busqueda) |
            Q(fkMascota__idMascota__icontains = busqueda)
        ).distinct()


    return render (request, 'mostrarTratamiento.html', {'tratamientos': tratamientos})

@login_required
def registarAdopciones (request):

    context = {}

    if request.method == 'POST':

        form = FormularioMascotaAdopcion(request.POST, request.FILES)

        if form.is_valid():

            nom = form.cleaned_data.get('nombre')
            esp = form.cleaned_data.get('especie')
            raz = form.cleaned_data.get('raza')
            ed = form.cleaned_data.get('edad')
            sex = form.cleaned_data.get('sexo')
            cas = form.cleaned_data.get('castrado')
            fot = form.cleaned_data.get('foto')
            des = form.cleaned_data.get('descripcion')

            adopcion = mascotasAdopciones.objects.create(

                nombre = nom,
                especie = esp,
                raza = raz,
                edad = ed,
                sexo = sex,
                castrado = cas,
                foto = fot,
                descripcion = des

            )

            adopcion.save()

            form = FormularioMascotaAdopcion()

            return redirect('/mostrarAdopcion/')
        
    else:

        form = FormularioMascotaAdopcion()

    context['form'] = form

    return render(request, 'registrarAdopcion.html', context)


def mostrarAdopcion (request):

    queryset = request.GET.get("buscar")

    adopciones = mascotasAdopciones.objects.all()

    if queryset:
        
        adopciones = mascotasAdopciones.objects.filter(
            
            Q(especie__icontains = queryset) | 
            Q(raza__icontains = queryset) |
            Q(edad__icontains = queryset) |
            Q(sexo__icontains = queryset) |
            Q(nombre__icontains = queryset)
            
        ).distinct()

    
        
    return render (request, 'mostrarAdopcion.html', {'adopciones': adopciones})
 

def salir (request):

    logout (request)

    return redirect ('/')




