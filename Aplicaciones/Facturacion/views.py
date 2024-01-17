from django.shortcuts import render, redirect
from .models import GeneroLiterario
from .models import Profesion
from .models import Autor
from .models import Libro

from django.contrib import messages
# Create your views here.
def listadoGeneros(request):
    generoBdd = GeneroLiterario.objects.all()
    return render(request, 'listadoGeneros.html', {'generos': generoBdd})


def guardarGenero(request):
    nombre_bg=request.POST["nombre_bg"]
    descripcion_bg=request.POST["descripcion_bg"]
    fotografia_referencia=request.FILES.get("fotografia_referencia")
    #Insertando datos mediante el ORM de django
    genero =GeneroLiterario.objects.create(nombre_bg=nombre_bg,descripcion_bg=descripcion_bg,fotografia_referencia=fotografia_referencia)
    messages.success(request, 'GENERO LITERARIO GUARDADO EXITOSAMENTE')
    return redirect('/')


def eliminarGenero(request,id_bg):
    generoEliminar=GeneroLiterario.objects.get(id_bg=id_bg)
    generoEliminar.delete()
    messages.success(request, 'GENERO LITERARIO ELIMINADA EXITOSAMENTE')
    return redirect('/')

def editarGenero(request, id_bg):
    generoEditar=GeneroLiterario.objects.get(id_bg=id_bg)
    generosBdd=GeneroLiterario.objects.all()
    return  render(request, 'editarGenero.html',{'genero':generoEditar,'generos':generosBdd})



def procesarActualizacionGenero(request):
    id_bg=request.POST["id_bg"]
    nombre_bg=request.POST["nombre_bg"]
    descripcion_bg=request.POST["descripcion_bg"]
    fotografia_referencia=request.POST["fotografia_referencia"]

    #Insertando datos mediante el ORM de DJANGO
    generoEditar=GeneroLiterario.objects.get(id_bg=id_bg)
    generoEditar.nombre_bg=nombre_bg
    generoEditar.descripcion_bg=descripcion_bg
    generoEditar.fotografia_referencia=fotografia_referencia
    generoEditar.save()
    messages.success(request,
      'GENERO LITERARIO ACTUALIZADO EXITOSAMENTE')
    return redirect('/')


def listadoProfesiones(request):
    profesionBdd = Profesion.objects.all()
    return render(request, 'listadoProfesiones.html', {'profesiones': profesionBdd})

def guardarProfesion(request):
    nombre_bg=request.POST["nombre_bg"]
    descripcion_bg=request.POST["descripcion_bg"]

    #Insertando datos mediante el ORM de django
    profesion =Profesion.objects.create(nombre_bg=nombre_bg,descripcion_bg=descripcion_bg)
    messages.success(request, 'PROFESION  GUARDADA EXITOSAMENTE')
    return redirect('/listadoProfesiones/')

def eliminarProfesion(request,id_bg):
    profesionEliminar=Profesion.objects.get(id_bg=id_bg)
    profesionEliminar.delete()
    messages.success(request, 'PROFESION ELIMINADA EXITOSAMENTE')
    return redirect('/listadoProfesiones/')

def editarProfesion(request, id_bg):
    profesionEditar=Profesion.objects.get(id_bg=id_bg)
    profesionesBdd=Profesion.objects.all()
    return  render(request, 'editarProfesion.html',{'profesion':profesionEditar,'profesiones':profesionesBdd})

def procesarActualizacionProfesion(request):
    id_bg=request.POST["id_bg"]
    nombre_bg=request.POST["nombre_bg"]
    descripcion_bg=request.POST["descripcion_bg"]

    #Insertando datos mediante el ORM de DJANGO
    profesionEditar=Profesion.objects.get(id_bg=id_bg)
    profesionEditar.nombre_bg=nombre_bg
    profesionEditar.descripcion_bg=descripcion_bg
    profesionEditar.save()
    messages.success(request,
      'PROFESION ACTUALIZADA EXITOSAMENTE')
    return redirect('/listadoProfesiones/')



def listadoAutores(request):
    autoresBdd = Autor.objects.all()
    profesionBdd = Profesion.objects.all()

    return render(request, 'listadoAutores.html', {'autores': autoresBdd, 'profesiones': profesionBdd})

def eliminarAutor(request,id_bg):
    autorEliminar=Autor.objects.get(id_bg=id_bg)
    autorEliminar.delete()
    messages.success(request, 'AUTOR ELIMINADO EXITOSAMENTE')
    return redirect('/listadoAutores/')

def guardarAutor(request):
    id_profesion=request.POST["id_profesion"]
    #capturando el tipo seleccionado por el usuario
    profesionSeleccionado=Profesion.objects.get(id_bg=id_profesion)

    apellido_bg=request.POST["apellido_bg"]
    nombre_bg=request.POST["nombre_bg"]
    edad_bg=request.POST["edad_bg"]

    fotografia_portada=request.FILES.get("fotografia_portada")

    #Insertando datos mediante el ORM de django

    autor = Autor.objects.create(
        apellido_bg=apellido_bg,
        nombre_bg=nombre_bg,
        edad_bg=edad_bg,
        profesion_bg=profesionSeleccionado,
        fotografia_portada=fotografia_portada,

    )

    messages.success(request, 'AUTOR GUARDADO EXITOSAMENTE')
    return redirect('/listadoAutores/')


def editarAutor(request, id_bg):
    autorEditar=Autor.objects.get(id_bg=id_bg)
    profesionesBdd = Profesion.objects.all()
    return  render(request, 'editarAutor.html',{'autor':autorEditar, 'profesiones': profesionesBdd})


def procesarActualizacionAutor(request):
    # Obtener los datos del formulario
    id_bg = request.POST["id_bg"]
    id_profesion = request.POST["id_profesion"]
    profesionSeleccionado = Profesion.objects.get(id_bg=id_profesion)
    apellido_bg = request.POST["apellido_bg"]
    nombre_bg = request.POST["nombre_bg"]
    edad_bg = request.POST["edad_bg"]

    # Verificar si 'fotografia' está presente en request.FILES
    if 'fotografia_portada' in request.FILES:
        fotografia_portada = request.FILES['fotografia_portada']

        # Guardar el archivo en el sistema de archivos
        with default_storage.open(f"autor_fotografias/{id_bg}_{fotografia_portada.name}", 'wb') as destination:
            for chunk in fotografia_portada.chunks():
                destination.write(chunk)

        # Asignar la ruta del archivo al campo 'fotografia' en el modelo
        fotografia_path = f"autor_fotografias/{id_bg}_{fotografia_portada.name}"
    else:
        fotografia_path = None

    # Actualizar el propietario con los nuevos datos
    autorEditar = Autor.objects.get(id_bg=id_bg)
    autorEditar.profesion = profesionSeleccionado
    autorEditar.apellido_bg = apellido_bg
    autorEditar.nombre_bg = nombre_bg
    autorEditar.edad_bg = edad_bg


    if fotografia_path:
        autorEditar.fotografia_portada = fotografia_path

    autorEditar.save()

    messages.success(request, 'AUTOR ACTUALIZADO EXITOSAMENTE')
    return redirect('/listadoAutores/')

def listadoLibros(request):
    librosBdd = Libro.objects.all()
    generoBdd = GeneroLiterario.objects.all()
    autorBdd = Autor.objects.all()


    return render(request, 'listadoLibros.html', {'libros': librosBdd, 'generos': generoBdd, 'autores': autorBdd})

def eliminarLibro(request,id_bg):
    libroEliminar=Libro.objects.get(id_bg=id_bg)
    libroEliminar.delete()
    messages.success(request, 'LIBRO ELIMINADO EXITOSAMENTE')
    return redirect('/listadoLibros/')


def guardarLibro(request):
    id_genero=request.POST["id_genero"]
    id_autor=request.POST["id_autor"]
    #capturando el tipo seleccionado por el usuario
    generoSeleccionado=GeneroLiterario.objects.get(id_bg=id_genero)
    autorSeleccionado=Autor.objects.get(id_bg=id_autor)

    titulo_bg=request.POST["titulo_bg"]
    editorial_bg=request.POST["editorial_bg"]
    fecha_publicacion_bg=request.POST["fecha_publicacion_bg"]
    fotografia_portada=request.FILES.get("fotografia_portada")

    #Insertando datos mediante el ORM de django

    libro = Libro.objects.create(
        titulo_bg=titulo_bg,
        editorial_bg=editorial_bg,
        fecha_publicacion_bg=fecha_publicacion_bg,
        genero_bg=generoSeleccionado,
        autor_bg=autorSeleccionado,
        fotografia_portada=fotografia_portada,

    )

    messages.success(request, 'LIBRO GUARDADO EXITOSAMENTE')
    return redirect('/listadoLibros/')

def editarLibro(request, id_bg):
    libroEditar=Libro.objects.get(id_bg=id_bg)
    generosBdd = GeneroLiterario.objects.all()
    autoresBdd = Autor.objects.all()
    return  render(request, 'editarLibro.html',{'libro':libroEditar, 'generos': generosBdd, 'autores': autoresBdd})


def procesarActualizacionLibro(request):
    # Obtener los datos del formulario
    id_bg = request.POST["id_bg"]
    id_genero = request.POST["id_genero"]
    id_autor = request.POST["id_autor"]
    generoSeleccionado = GeneroLiterario.objects.get(id_bg=id_genero)
    autorSeleccionado = Autor.objects.get(id_bg=id_autor)
    titulo_bg = request.POST["titulo_bg"]
    editorial_bg = request.POST["editorial_bg"]
    fecha_publicacion_bg = request.POST["fecha_publicacion_bg"]


    # Verificar si 'fotografia' está presente en request.FILES
    if 'fotografia_portada' in request.FILES:
        fotografia = request.FILES['fotografia_portada']

        # Guardar el archivo en el sistema de archivos
        with default_storage.open(f"libro_fotografias/{id_bg}_{fotografia.name}", 'wb') as destination:
            for chunk in fotografia.chunks():
                destination.write(chunk)

        # Asignar la ruta del archivo al campo 'fotografia' en el modelo
        fotografia_path = f"libro_fotografias/{id_bg}_{fotografia.name}"
    else:
        fotografia_path = None

    # Actualizar el propietario con los nuevos datos
    libroEditar = Libro.objects.get(id_bg=id_bg)
    libroEditar.genero = generoSeleccionado
    libroEditar.autor = autorSeleccionado
    libroEditar.titulo_bg = titulo_bg
    libroEditar.editorial_bg = editorial_bg
    libroEditar.fecha_publicacion_bg = fecha_publicacion_bg

    if fotografia_path:
        libroEditar.fotografia = fotografia_path

    libroEditar.save()

    messages.success(request, 'LIBRO ACTUALIZADO EXITOSAMENTE')
    return redirect('/listadoLibros/')
