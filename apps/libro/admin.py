from django.contrib import admin
from .models import Autor, Libro

#Para añadir a panel de control de Django
admin.site.register(Autor)
admin.site.register(Libro)

