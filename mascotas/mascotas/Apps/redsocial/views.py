from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Usuario, Pet, Comentario
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .forms import FormUsuarios, FormPet, FormComentario


# Create your views here.
def usuario(request):
    data = {
        'form': FormUsuarios()  
    }
    return render(request,'formulario.html', data )

def index(request):
    usuario = Usuario.objects.order_by('Rut')
    pet = Pet.objects.order_by('Nombre')
    context = {'usuario': usuario,'pet': pet}
    return render(request, 'login.html', context)

def index2(request):
	pe= Pet.objects.get(Nombre='Firulais')
	context = {'perro': pe}
	return render(request, 'caca.html', context)

def base(request):

    return render(request, 'base_generic.html', )


def inicio(request):

    return render(request, 'index.html', )


#informacion ANIMALES

def college(request):

    return render(request, 'college.html', )


def veterinarios(request):

    return render(request, 'veterinarios.html', )


def animalcosas(request):

    return render(request, 'animalcosas.html', )

def testimonio(request):

    return render(request, 'testimonio.html', )


def contacto(request):

    return render(request, 'contacto.html', )


def login(request):

    return index(request)

def pet_form(request):
    data = {
        'formu': FormPet()  
    }

    if request.method == 'POST':
        formu_pet = FormPet(data=request.POST)
        if formu_pet.is_valid():
            formu_pet.save()
            data['mensaje'] = 'Registrado correctamente'
        else:
            data['form'] = formu_pet
    
    return render(request,'p_usuario.html', data )

def resultado(request,rut):
	pe= Usuario.objects.get(Rut=rut)
	mas= Pet.objects.filter(Amo=rut)
	context = {'due': pe,'mascotas':mas}
	return render(request, 'resultado.html', context)


    #comentario o testimonio
    
def comentario_form(request):
    data = {
        'formu1': FormComentario()  
    }
    if request.method == 'POST':
        formu1_comentario = FormComentario(data=request.POST)
        if formu1_comentario.is_valid():
            formu1_comentario.save()
            data['mensaje'] = 'Comentario Registrado correctamente'
        else:
            data['form'] = formu1_comentario
    
    return render(request,'comentario.html', data )

