from django.shortcuts import render
from django.http import HttpResponse
from ReproductorMusic2.models import *

def inicio(request):
    return HttpResponse("<h1>Bienvenido a reproductor favorito</h1>")

def inicio(request):
    lista_cancion = Cancion.objects.all()
    lista_genero = Genero.objects.all()
    return render(request, "index.html",{"canciones":lista_cancion,'generos':lista_genero})

def login(request):
    return render(request, "login.html")

def autenticar(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        password = request.POST['password']

        if usuario in Usuario.objects.values_list('nick', flat=True) and password in Usuario.objects.values_list('contraseña', flat=True):
            usuario_autenticado = Usuario.objects.values('nick', 'nombre', 'apellido').distinct().filter(nick = usuario)
            lista_cancion = Cancion.objects.filter(usuario_nick = usuario)
            lista_genero = Genero.objects.all()
            return render(request, "index.html",{'usuario':usuario_autenticado, 'canciones':lista_cancion, 'generos':lista_genero})
        else:
            return render(request,"login.html")
def agregar_cancion(request):
        autor = request.POST['autor']
        titulo = request.POST['titulo']
        genero_id = request.POST['genero']
        ruta = request.POST['ruta']
        usuario_nick = request.POST['user']

        #CREAR UN OBJETO DEL TIPO USUARIO
        usuario = Usuario.objects.get(nick = usuario_nick)

        #CREAR UN OBJETO DEL TIPO CANCION
        cancion = Cancion()
        gen = Genero()
        gen.id = genero_id
        cancion.autor = autor
        cancion.titulo = titulo
        cancion.ruta = ruta
        cancion.genero = gen # el atributo genero es un objeto de tipo Genero
        cancion.usuario_nick = usuario # el atributo usuario_nick es un objeto de tipo Usuario

        cancion.save()

        lista_cancion = Cancion.objects.filter(usuario_nick = usuario)
        lista_genero = Genero.objects.all()
        return render(request, "index.html",{'usuario':usuario_autenticado, 'canciones':lista_cancion, 'generos':lista_genero})
