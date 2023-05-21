def agregar_inmueble(lista, inmueble):
    lista.append(inmueble)

def editar_inmueble(lista, indice, nuevos_datos):
    lista[indice].update(nuevos_datos)

def eliminar_inmueble(lista, indice):
    del lista[indice]

def cambiar_estado(lista, indice, nuevo_estado):
    lista[indice]['estado'] = nuevo_estado

def buscar_inmuebles(lista, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista:
        if (inmueble['estado'] in ['Disponible', 'Reservado'] and
                calcular_precio(inmueble) <= presupuesto):
            inmueble_con_precio = dict(inmueble)
            inmueble_con_precio['precio'] = calcular_precio(inmueble)
            inmuebles_encontrados.append(inmueble_con_precio)
    return inmuebles_encontrados

def calcular_precio(inmueble):
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']

    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    
    return precio
# Ejemplo de uso:
inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]
nuevo_inmueble=[]
# Agregar un nuevo inmueble
nuevo_inmueble = {'año': 2021, 'metros': 120, 'habitaciones': 3, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'}
agregar_inmueble(inmuebles, nuevo_inmueble)

# Editar el segundo inmueble
editar_inmueble(inmuebles, 1, {'metros': 85, 'garaje': True})

# Cambiar el estado del tercer inmueble
cambiar_estado(inmuebles, 2, 'Vendido')

# Buscar inmuebles con un presupuesto dado
presupuesto_dado = 150000
inmuebles_encontrados = buscar_inmuebles(inmuebles, presupuesto_dado)
for inmueble in inmuebles_encontrados:
    print(nuevo_inmueble)
