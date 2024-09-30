# Función para procesar datos
def procesar_datos(lista_numeros):
    resultado_total = 0
    for numero in lista_numeros:
        resultado_total += procesar_numero(numero)
    return resultado_total

def procesar_numero(numero):
    if numero % 2 == 0:
        return procesar_par(numero)
    else:
        return procesar_impar(numero)

def procesar_par(numero):
    if numero > 50:
        return numero * 2
    return numero

def procesar_impar(numero):
    if numero < 20:
        return -numero
    elif numero > 100:
        return sum(i * numero for i in range(3))
    return 0

# Función para calcular el total de una lista, con manejo de valores negativos
def calcular_total(lista):
    total = 0
    for valor in lista:
        if valor > 0:
            total += valor
        else:
            total += valor * -1  # Convierte valores negativos a positivos
    return total

# Función principal para ejecutar el código
def main():
    # Lista de ejemplo para procesar_datos
    lista_datos = [10, 25, 60, 150, 7, 99, 120]
    print("Procesando la lista:", lista_datos)
    resultado = procesar_datos(lista_datos)
    print("Resultado de procesar_datos:", resultado)

    # Otra lista de ejemplo para calcular_total
    lista = [10, -20, 30, -40, 50]
    print("Calculando el total de la lista:", lista)
    total = calcular_total(lista)
    print("Resultado de calcular_total:", total)

# Ejecutar la función principal
main()
