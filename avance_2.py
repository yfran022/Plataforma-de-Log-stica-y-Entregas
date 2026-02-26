import os
os.system("cls")

def registrar_pedido(cliente, direccion="No especificada", telefono="No registrado", **kwargs):
    pedido = {
        "cliente": cliente,
        "direccion": direccion,
        "telefono": telefono
    }
    pedido.update(kwargs)
    return pedido

def motor_rutas(*args):
    zonas = {
        "marbella": {"km": 10, "precio": 10000},
        "torices": {"km": 15, "precio": 25000},
        "bicentenario": {"km": 30, "precio": 70000}
    }

    resultado = {}

    for zona in args:
        if zona in zonas:
            resultado[zona] = zonas[zona]

    return resultado


def asignar_repartidor(zona, **kwargs):
    trabajadores = {
        "yudis": ["marbella"],
        "jose": ["torices"],
        "gabriela": ["bicentenario"],
        "sara": ["marbella", "torices"]
    }

    for nombre, zonas in trabajadores.items():
        if zona in zonas:
            return nombre

    return "No disponible"



def calcular_tarifa(precio_producto=0, valor_envio=0):
    return precio_producto + valor_envio



cliente = input("Nombre del cliente: ")
direccion = input("Dirección: ")
telefono = input("Teléfono: ")

print("\nSeleccione la zona:")
print("1. Marbella - 10 km - $10000")
print("2. Torices  - 15 km - $25000")
print("3. bicentenario  - 30 km - $70000")

try:
    opcion = int(input("Ingrese el número de la zona: "))
except ValueError:
    print("Entrada inválida. Por favor ingrese un número.")
    exit()

zonas_lista = ["marbella", "torices", "bicentenario"]

if opcion in [1, 2, 3]:
    zona = zonas_lista[opcion - 1]
else:
    print("Opción inválida")
    exit()

producto = input("Producto: ")
precio_producto = float(input("Precio del producto: "))

# Registro del pedido
pedido = registrar_pedido(cliente, direccion=direccion, telefono=telefono)

# Motor de rutas
datos_ruta = motor_rutas(zona)

if zona in datos_ruta:
    valor_envio = datos_ruta[zona]["precio"]
    km = datos_ruta[zona]["km"]
else:
    valor_envio = 0
    km = 0

# Asignación de repartidor
repartidor = asignar_repartidor(zona)

# Desempaquetado para cálculo
datos_pago = {
    "precio_producto": precio_producto,
    "valor_envio": valor_envio
}

total_pagar = calcular_tarifa(**datos_pago)

print("\n===== SmartDelivery =====")
print(f"Cliente: {pedido['cliente']}")
print(f"Dirección: {pedido['direccion']}")
print(f"Teléfono: {pedido['telefono']}")
print(f"Zona: {zona}")
print(f"Distancia: {km} km")
print(f"Valor envío: ${valor_envio}")
print(f"Repartidor asignado: {repartidor}")
print(f"Total a pagar: ${total_pagar}")
