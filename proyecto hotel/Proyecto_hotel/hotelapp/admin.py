from django.contrib import admin
from .models import Habitacion,Hotel,Pago,Reserva,Rol,Usuario

# Register your models here.
admin.site.register(Habitacion)
admin.site.register(Hotel)
admin.site.register(Pago)
admin.site.register(Reserva)
admin.site.register(Rol)
admin.site.register(Usuario)