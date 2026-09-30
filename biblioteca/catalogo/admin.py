from django.contrib import admin
from .models import Libro, Reserva

# Register your models here.
admin.site.register(Libro)
admin.site.register(Reserva)