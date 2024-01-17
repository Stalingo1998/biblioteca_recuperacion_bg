from django.urls import path
from . import views

urlpatterns=[
    path('',views.listadoGeneros),
    path('guardarGenero/',views.guardarGenero),
    path('eliminarGenero/<id_bg>' ,views.eliminarGenero),
    path('editarGenero/<id_bg>' ,views.editarGenero),
    path('procesarActualizacionGenero/', views.procesarActualizacionGenero),
    path('listadoProfesiones/',views.listadoProfesiones),
    path('guardarProfesion/',views.guardarProfesion),
    path('eliminarProfesion/<id_bg>' ,views.eliminarProfesion),
    path('editarProfesion/<id_bg>' ,views.editarProfesion),
    path('procesarActualizacionProfesion/', views.procesarActualizacionProfesion),
    path('listadoAutores/',views.listadoAutores),
    path('eliminarAutor/<id_bg>' ,views.eliminarAutor),
    path('guardarAutor/',views.guardarAutor),
    path('editarAutor/<id_bg>' ,views.editarAutor),
    path('procesarActualizacionAutor/', views.procesarActualizacionAutor),
    path('listadoLibros/',views.listadoLibros),
    path('eliminarLibro/<id_bg>' ,views.eliminarLibro),
    path('guardarLibro/',views.guardarLibro),
    path('editarLibro/<id_bg>' ,views.editarLibro),
    path('procesarActualizacionLibro/', views.procesarActualizacionLibro),












]
