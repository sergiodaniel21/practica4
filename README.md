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
