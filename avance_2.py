import os
os.system("cls")

def envios(nombre, direccion, telefono):
    return nombre, direccion, telefono

nombre    = input("Ingrese su nombre para realizar el pedido: ")
direccion = input("Ingrese su dirección para realizar el pedido: ")
telefono  = input("Ingrese su teléfono para realizar el pedido: ")

info_envio = envios(nombre, direccion, telefono)

print(f"\nCliente: {info_envio[0]} | Dirección: {info_envio[1]} | Teléfono: {info_envio[2]}")


def rutas(barrio, km):
    return barrio, km

barrio            = ["Marbella", "Torices",  "Biatona"]
km                = [10,          15,         30]
nombre_repartidor = ["sara",      "jorge",      "juan"]

print("\nSeleccione el barrio:")
print("0. Marbella - 10 km")
print("1. Torices  - 15 km")
print("2. Biatona  - 30 km")

selectbarrio = int(input("Escoge el número del barrio: "))

info_ruta = rutas(barrio[selectbarrio], km[selectbarrio])

print(f"Barrio seleccionado: {info_ruta[0]} | Distancia: {info_ruta[1]} km")



def tarifas(km):
    tarifa_base   = 1000
    precio_por_km = 1000
    total = tarifa_base + (km * precio_por_km)
    return total

total_pagar = tarifas(info_ruta[1])

print(f"Tarifa del envío: ${total_pagar}")


def repartidores(ruta, nombre):
    return ruta, nombre

info_repartidor = repartidores(barrio[selectbarrio], nombre_repartidor[selectbarrio])

print(f"Repartidor asignado: {info_repartidor[1]} | Ruta: {info_repartidor[0]}")


print("\n SmartDelivery ")
print(f"Cliente:    {info_envio[0]}")
print(f"Barrio:     {info_ruta[0]}")
print(f"Distancia:  {info_ruta[1]} km")
print(f"Total:      ${total_pagar}")
print(f"Repartidor: {info_repartidor[1]}")