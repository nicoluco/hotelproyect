from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Habitacion(models.Model):
    habitacion_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    n_banos = models.IntegerField(blank=True, null=True)
    metroscuadrados = models.CharField(db_column='metrosCuadrados', max_length=5, blank=True, null=True)  # Field name made lowercase.
    disponibilidad = models.IntegerField(blank=True, null=True)
    tarifa = models.IntegerField(blank=True, null=True)
    hotel = models.ForeignKey('Hotel', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habitacion'


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)
    ubicacion = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    monto = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Usuario', models.DO_NOTHING)
    id_habitacion = models.ForeignKey(Habitacion, models.DO_NOTHING, db_column='id_habitacion')
    id_pago = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    fecha_inicio = models.DateField(db_column='fecha-inicio', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    fecha_termino = models.DateField(db_column='fecha-termino', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'reserva'


class Rol(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rol'
        db_table_comment = 'roles'


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10, blank=True, null=True)
    appellido = models.CharField(max_length=10, blank=True, null=True)
    correo = models.CharField(max_length=25, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol', blank=True, null=True)
    
    #user de django pa iniciar sesion
    djuser = models.OneToOneField(User,on_delete=models.CASCADE)  #foreign key para unirlo al user django

    class Meta:
        managed = False
        db_table = 'usuario'
