from django.shortcuts import render
from .models import Cliente,Pedido

# Create your views here.
def listclients(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes.html",{"clientes":clientes})

def listpedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos.html", {"pedidos":pedidos})