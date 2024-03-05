
import pulp as lp
import matplotlib.pyplot as plt

#Conjuntos

cables = ['Encauchetado de cobre', 'Coaxial', 'Fibra óptica']
semanas = list(range(1, 15))

#Parametros

costo_compra = {
    (1, 'Encauchetado de cobre'): 6097,
    (1, 'Coaxial'): 2000,
    (1, 'Fibra óptica'): 2686,
    (2, 'Encauchetado de cobre'): 6430,
    (2, 'Coaxial'): 2012,
    (2, 'Fibra óptica'): 2590,
    (3, 'Encauchetado de cobre'): 6205,
    (3, 'Coaxial'): 1960,
    (3, 'Fibra óptica'): 2457,
    (4, 'Encauchetado de cobre'): 6090,
    (4, 'Coaxial'): 2592,
    (4, 'Fibra óptica'): 2910,
    (5, 'Encauchetado de cobre'): 5847,
    (5, 'Coaxial'): 2550,
    (5, 'Fibra óptica'): 2628,
    (6, 'Encauchetado de cobre'): 5625,
    (6, 'Coaxial'): 2621,
    (6, 'Fibra óptica'): 2727,
    (7, 'Encauchetado de cobre'): 5208,
    (7, 'Coaxial'): 2705,
    (7, 'Fibra óptica'): 2238,
    (8, 'Encauchetado de cobre'): 9450,
    (8, 'Coaxial'): 2566,
    (8, 'Fibra óptica'): 2771,
    (9, 'Encauchetado de cobre'): 6927,
    (9, 'Coaxial'): 2303,
    (9, 'Fibra óptica'): 2766,
    (10, 'Encauchetado de cobre'): 6433,
    (10, 'Coaxial'): 2551,
    (10, 'Fibra óptica'): 2770,
    (11, 'Encauchetado de cobre'): 7250,
    (11, 'Coaxial'): 2036,
    (11, 'Fibra óptica'): 3061,
    (12, 'Encauchetado de cobre'): 6058,
    (12, 'Coaxial'): 2442,
    (12, 'Fibra óptica'): 2828,
    (13, 'Encauchetado de cobre'): 6802,
    (13, 'Coaxial'): 2722,
    (13, 'Fibra óptica'): 3208,
    (14, 'Encauchetado de cobre'): 6851,
    (14, 'Coaxial'): 2679,
    (14, 'Fibra óptica'): 2610 }

costo_tercero = {
    'Encauchetado de cobre': 6755,
    'Coaxial': 3035,
    'Fibra óptica': 3550
}

inventario_inicial = {
    'Encauchetado de cobre': 687,
    'Coaxial': 6070,
    'Fibra óptica': 566
}

requerimiento = {
    (1, 'Encauchetado de cobre'): 728,
    (1, 'Coaxial'): 20740,
    (1, 'Fibra óptica'): 257,
    (2, 'Encauchetado de cobre'): 645,
    (2, 'Coaxial'): 18898,
    (2, 'Fibra óptica'): 236,
    (3, 'Encauchetado de cobre'): 692,
    (3, 'Coaxial'): 20161,
    (3, 'Fibra óptica'): 247,
    (4, 'Encauchetado de cobre'): 742,
    (4, 'Coaxial'): 19910,
    (4, 'Fibra óptica'): 259,
    (5, 'Encauchetado de cobre'): 914,
    (5, 'Coaxial'): 25607,
    (5, 'Fibra óptica'): 270,
    (6, 'Encauchetado de cobre'): 744,
    (6, 'Coaxial'): 20360,
    (6, 'Fibra óptica'): 330,
    (7, 'Encauchetado de cobre'): 620,
    (7, 'Coaxial'): 19453,
    (7, 'Fibra óptica'): 370,
    (8, 'Encauchetado de cobre'): 888,
    (8, 'Coaxial'): 22572,
    (8, 'Fibra óptica'): 357,
    (9, 'Encauchetado de cobre'): 865,
    (9, 'Coaxial'): 23042,
    (9, 'Fibra óptica'): 350,
    (10, 'Encauchetado de cobre'): 842,
    (10, 'Coaxial'): 22452,
    (10, 'Fibra óptica'): 217,
    (11, 'Encauchetado de cobre'): 875,
    (11, 'Coaxial'): 19870,
    (11, 'Fibra óptica'): 214,
    (12, 'Encauchetado de cobre'): 672,
    (12, 'Coaxial'): 21810,
    (12, 'Fibra óptica'): 230,
    (13, 'Encauchetado de cobre'): 680,
    (13, 'Coaxial'): 22996,
    (13, 'Fibra óptica'): 292,
    (14, 'Encauchetado de cobre'): 672,
    (14, 'Coaxial'): 25013,
    (14, 'Fibra óptica'): 248}

inventario_minimo = {
    'Encauchetado de cobre': 135,
    'Coaxial': 660,
    'Fibra óptica': 70
}

inventario_maximo = {
    'Encauchetado de cobre': 7300,
    'Coaxial': 7300,
    'Fibra óptica': 7300
}

capacidad_compra = {
    'Encauchetado de cobre': 950,
    'Coaxial': 21335,
    'Fibra óptica': 305
}

costo_inventario = 290
presupuesto = 6000000
capacidad_bodega = 7300


# Inicialización del modelo
modelo = lp.LpProblem('Planeación de abastecimiento', lp.LpMinimize)

# Variables de decisión
x = lp.LpVariable.dicts('CompraProveedor', (semanas, cables), lowBound=0, cat='Continuous')
y = lp.LpVariable.dicts('CompraTercero', (semanas, cables), lowBound=0, cat='Continuous')
inventario_final_semana = lp.LpVariable.dicts('InventarioFinal', (semanas, cables), lowBound=0, cat='Continuous')

# Función objetivo
modelo += lp.lpSum((costo_compra[(t, c)] * x[t][c]) + (costo_tercero[c] * y[t][c])  for c in cables for t in semanas)

# Restricciones

# Flujo de inventario para la semana 1
for c in cables:
    modelo += inventario_final_semana[1][c] == inventario_inicial[c] + x[1][c] - requerimiento[(1, c)]

# Flujo de inventario para la semana 2 en adelante
for c in cables:
    for t in semanas:  # Empezando desde la semana 2 hasta la 14
        if t == 2:
            modelo += inventario_final_semana[t][c] == inventario_final_semana[t-1][c] + x[t][c] - requerimiento[(t, c)]
        elif t > 2:
            # Agregando compras al tercero con retraso de dos semanas
            modelo += inventario_final_semana[t][c] == inventario_final_semana[t-1][c] + x[t][c] + y[t-2][c] - requerimiento[(t, c)]

# Mantener inventario mínimo para todas las semanas excepto la 14
for c in cables:
    for t in semanas:
        if t != 14: # Excluye la última semana
            modelo += inventario_final_semana[t][c] >= inventario_minimo[c]

# Capacidad máxima de compra semanal del proveedor
for c in cables:
    for t in semanas:
        modelo += x[t][c] <= capacidad_compra[c]

# Capacidad total de la bodega
for t in semanas:
    modelo += lp.lpSum(inventario_final_semana[t][c] for c in cables) <= capacidad_bodega

# Presupuesto total para almacenamiento
modelo += lp.lpSum(costo_inventario * inventario_final_semana[t][c] for c in cables for t in semanas) <= presupuesto

# Resolver el modelo
modelo.solve()

# Verificar el estado del modelo y mostrar los resultados
print("Estado de la solución:", lp.LpStatus[modelo.status])
print("Costo total optimizado: $", lp.value(modelo.objective))

# Mostrar decisiones de compra y niveles de inventario
for c in cables:
    for t in semanas:
        print(f"Semana {t}, Cable {c}: Compra Proveedor = {x[t][c].value()}, Compra Tercero = {y[t][c].value()}, Inventario Final = {inventario_final_semana[t][c].value()}")
        
#Graficas

# Graficar las decisiones de compra

fig, ax = plt.subplots(3, 1, figsize=(10, 15))

plt.subplots_adjust(hspace=0.5)
for i, c in enumerate(cables):
    compras_proveedor = [x[t][c].value() for t in semanas]
    compras_tercero = [y[t][c].value() for t in semanas]
    ax[i].plot(semanas, compras_proveedor, label='Compra Proveedor', marker='o')
    ax[i].plot(semanas, compras_tercero, label='Compra Tercero', marker='x')
    ax[i].set_xlabel('Semanas')
    ax[i].set_ylabel('Cantidad')
    ax[i].set_title(f'Compras de {c}')
    ax[i].legend()
plt.show()

# Graficar los niveles de inventario

fig, ax = plt.subplots(3, 1, figsize=(10, 15))

plt.subplots_adjust(hspace=0.5)
for i, c in enumerate(cables):
    inventario = [inventario_final_semana[t][c].value() for t in semanas]
    ax[i].plot(semanas, inventario, label='Inventario Final', marker='o')
    ax[i].set_xlabel('Semanas')
    ax[i].set_ylabel('Cantidad')
    ax[i].set_title(f'Inventario de {c}')
    ax[i].legend()
plt.show()

# Graficar el costo total a lo largo del tiempo

for t in semanas:
    costo_total = lp.value(lp.lpSum((costo_compra[(t, c)] * x[t][c]) + (costo_tercero[c] * y[t][c]) + (costo_inventario * inventario_final_semana[t][c]) for c in cables))
    plt.plot(t, costo_total, marker='o', color='b')
    plt.xlabel('Semanas')
    plt.ylabel('Costo total')
    plt.title('Costo total a lo largo del tiempo')
plt.show()

