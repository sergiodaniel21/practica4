# Función para procesar datos
def procesar_datos(lista_datos):
    resultado = 0
    for dato in lista_datos:
        if dato % 2 == 0:  # Verifica si el número es par
            if dato > 50:
                resultado += dato * 2
            else:
                resultado += dato
        else:  # Si es impar
            if dato < 20:
                resultado -= dato
            elif dato > 100:
                for i in range(3):
                    resultado += i * dato
    return resultado

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
