#Fredi: defini como calcular el precio
def calcular_precio(inmueble):
    antiguedad = 2023 - inmueble['año']
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    
    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 + garaje * 1500) * (1 - antiguedad / 100) * 2
    
    return precio
