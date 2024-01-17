from django.contrib import admin
from .models import  GeneroLiterario
from .models import  Profesion
from .models import  Autor
from .models import  Libro
# Register your models here.
admin.site.register(GeneroLiterario)
admin.site.register(Profesion)
admin.site.register(Autor)
admin.site.register(Libro)
