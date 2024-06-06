from .models import Chofer, Vehiculo, RegistroContabilidad
from django.utils import timezone

def crear_vehiculo(patente, marca, modelo, year):
    vehiculo = Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, year=year)
    return vehiculo

def crear_chofer(rut, nombre, apellido):
    chofer = Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido)
    return chofer

def crear_registro_contable(vehiculo, fecha_compra, valor):
    registro = RegistroContabilidad.objects.create(vehiculo=vehiculo, fecha_compra=fecha_compra, valor=valor)
    return registro

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()
    return chofer

def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer = Chofer.objects.filter(vehiculo=vehiculo).first()
    if chofer:
        chofer.activo = False
        chofer.save()
    return vehiculo

def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()
    return chofer

def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer = Chofer.objects.filter(vehiculo=vehiculo).first()
    if chofer:
        chofer.activo = True
        chofer.save()
    return vehiculo

def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    return vehiculo

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    return chofer

def asignar_chofer_a_vehiculo(rut, patente):
    chofer = Chofer.objects.get(rut=rut)
    vehiculo = Vehiculo.objects.get(patente=patente)
    chofer.vehiculo = vehiculo
    chofer.save()
    return chofer

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        chofer = Chofer.objects.filter(vehiculo=vehiculo).first()
        print(f"Vehículo: {vehiculo.marca} {vehiculo.modelo} ({vehiculo.patente})")
        if chofer:
            print(f"   Chofer: {chofer.nombre} {chofer.apellido} ({chofer.rut})")
        else:
            print("   Chofer: No asignado")
