
"""Optiobras es una empresa dedicada a construir desarrollos
urbanísticos en la periferia de la ciudad de Bucaramanga.
En los próximos meses, la empresa comenzará el proyecto
más grande que ha realizado y que tiene un impacto en
cerca de 350 viviendas. En particular, la empresa se
enfrenta al reto de manejar tres tipos de cables que se
usarán en la construcción: cable encauchetado de cobre,
cable coaxial y cable de fibra óptica. El comité de
planeación del proyecto ha solicitado su asesoría para
optimizar la planeación del abastecimiento de dichos tipos
de cables durante las primeras 14 semanas del proyecto.
Optiobras tiene un contrato con un proveedor para la compra de los cables. Para realizar la
planeación, se debe tener en cuenta que las órdenes al proveedor se realizan el primer día
de la semana y, como consecuencia, el material asociado a la orden puede ser utilizado esa
misma semana. Por otra parte, el costo unitario de compra de los cables varía según la
semana en que se compren. Esto debido a que este costo se fija con base a una estimación
del precio del dólar pues la materia prima se debe importar. Los costos se encuentran en la
Tabla 1.
Tabla 1. Costo unitario de compra al proveedor por semana y tipo de cable ($ COP/metro).
Encauchetado
de cobre Coaxial Fibra
óptica
Encauchetado
de cobre Coaxial Fibra
óptica
1 $ 6,097 $ 2,000 $ 2,686 8 $ 9,450 $ 2,566 $ 2,771
2 $ 6,430 $ 2,012 $ 2,590 9 $ 6,927 $ 2,303 $ 2,766
3 $ 6,205 $ 1,960 $ 2,457 10 $ 6,433 $ 2,551 $ 2,770
4 $ 6,090 $ 2,592 $ 2,910 11 $ 7,250 $ 2,036 $ 3,061
5 $ 5,847 $ 2,550 $ 2,628 12 $ 6,058 $ 2,442 $ 2,828
6 $ 5,625 $ 2,621 $ 2,727 13 $ 6,802 $ 2,722 $ 3,208
7 $ 5,208 $ 2,705 $ 2,238 14 $ 6,851 $ 2,679 $ 2,610
Tipo de cable Tipo de cable
Semana Semana
En cualquier semana, se puede comprar más cable del requerido y almacenarlo en una
bodega para que sea utilizado en el futuro. La bodega de almacenamiento tiene una
capacidad total de 7,300 metros de cualquier tipo de cable y es monitoreada al finalizar
cada semana para contabilizar su nivel de inventario. Después de un estudio, se ha
determinado que el costo de tener un metro de cualquier tipo de cable en inventario
durante una semana es de $290 COP. Para evitar retrasos en la obra, Optiobras siempre
debe tener inventarios mínimos. Las cantidades mínimas que debe haber al final de cada
semana, en metros, son: 135 de cable encauchetado de cobre, 660 de cable coaxial y 70 de 
cable de fibra óptica. Tenga en cuenta que esta condición no aplica para el último periodo
de decisión. Es decir, no hay requerimiento mínimo de inventario para la semana 14.
El proveedor ha comunicado las cantidades máximas que puede enviar de cada tipo de
cable. En metros, estas cantidades son: 950 de cable encauchetado de cobre, 21,335 de
cable coaxial y 305 de cable de fibra óptica. Además, Optiobras está en contacto con un
tercero que tiene capacidad ilimitada de despacho. Con el tercero, un metro de cable
encauchetado de cobre, coaxial y de fibra óptica cuestan $6,755 COP, $3,035 COP y $3,550
COP, respectivamente. Es necesario tener en cuenta que el tiempo de entrega desde la
fábrica del tercero hasta la obra es de dos semanas. Es decir, si se realiza una compra al
inicio de la semana 1, la orden estará disponible en la obra al inicio de la semana 3.
En este momento, Optiobras cuenta con un inventario en bodega de 687 metros de cable
encauchetado de cobre, 6,070 metros de cable coaxial y 566 metros de cable de fibra óptica.
No hay órdenes en proceso o en camino del proveedor ni del tercero. El requerimiento en
metros de cable de cada tipo durante el horizonte de planeación se encuentra en la Tabla
2. Finalmente, por políticas de seguridad, es necesario limitar la cantidad de metros de cable
en inventario. En particular, se ha destinado un presupuesto de $6,000,000 COP para gastar
en el almacenamiento de cables en bodega a lo largo del horizonte de planeación. La
empresa busca cumplir con las metas de construcción de cada semana al menor costo de
compra, cumpliendo con las condiciones anteriormente mencionadas.
Tabla 2. Requerimiento de cable por semana y tipo de cable (metros)
Semana
Tipo de cable
Semana
Tipo de cable
Encauchetado
de cobre Coaxial Fibra
óptica
Encauchetado
de cobre Coaxial Fibra
óptica
1 728 20,740 257 8 888 22,572 357
2 645 18,898 236 9 865 23,042 350
3 692 20,161 247 10 842 22,452 217
4 742 19,910 259 11 875 19,870 214
5 914 25,607 270 12 672 21,810 230
6 744 20,360 330 13 680 22,996 292
7 620 19,453 370 14 672 25,013 248"""

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
modelo += lp.lpSum((costo_compra[(t, c)] * x[t][c]) + (costo_tercero[c] * y[t][c]) + (costo_inventario * inventario_final_semana[t][c]) for c in cables for t in semanas)

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

