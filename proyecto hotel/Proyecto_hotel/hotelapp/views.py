from django.shortcuts import render
from .models import Habitacion,Hotel,Pago,Reserva,Rol,Usuario

# Create your views here.
def index(request):
    context={
        'hoteles': Hotel.objects.all()
    }
    return render (request,'index.html',context)



def pagina2(request):
    context={}
    return render (request,'2.html',context)
