# Práctica 4: Revisión de Código

## Descripción
Este repositorio contiene el análisis y correcciones realizadas en el proyecto utilizando SonarLint.

## Violaciones y Correcciones

### 1. Violación: Complejidad Cognitiva
**Descripción**: La función `procesar_datos` tiene una alta complejidad cognitiva, lo que la hace difícil de entender y mantener.

**Corrección**: Refactorización de la función para disminuir la complejidad cognitiva dividiendo la lógica en funciones más pequeñas.

**Fragmento de Código Original**:
```python
def procesar_datos(lista_datos):
    resultado = 0
    for dato in lista_datos:
        if dato % 2 == 0:
            if dato > 50:
                resultado += dato * 2
            else:
                resultado += dato
        else:
            if dato < 20:
                resultado -= dato
            elif dato > 100:
                for i in range(3):
                    resultado += i * dato
    return resultado
```
**Fragmento de Código Refactorizado**:
```python
def procesar_datos(lista_datos):
    resultado = 0
    for dato in lista_datos:
        resultado += procesar_dato(dato)
    return resultado

def procesar_dato(dato):
    if dato % 2 == 0:
        return procesar_dato_par(dato)
    else:
        return procesar_dato_impar(dato)

def procesar_dato_par(dato):
    if dato > 50:
        return dato * 2
    else:
        return dato

def procesar_dato_impar(dato):
    if dato < 20:
        return -dato
    elif dato > 100:
        return sum(dato for i in range(3))
    return dato
```

### 2. Violación: Falta de manejo de errores
**Descripción**: No hay manejo de errores al procesar los datos, lo que podría causar que la aplicación falle con entradas inesperadas.

**Corrección**: Añadido manejo de excepciones.

**Fragmento de Código Original**:
```python
resultado = procesar_datos(lista_datos)
```
**Fragmento de Código Corregido**:
```python
try:
    resultado = procesar_datos(lista_datos)
except Exception as e:
    print(f"Error al procesar datos: {e}")
```
