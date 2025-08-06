# Proyecto: Función es_primo

Este proyecto contiene una función llamada `es_primo` que determina si un número es primo, junto con un conjunto completo de pruebas unitarias usando `pytest`.

## Estructura del proyecto

```
HW_C6/
├── func.py
├── func_test.py
└── README.md
```

## Descripción de los archivos

- **func.py**  
  Contiene la función `es_primo(num)`, que valida el tipo de parámetro y determina si un número es primo. Devuelve mensajes de error claros para entradas inválidas.

- **func_test.py**  
  Archivo de pruebas unitarias para `es_primo`. Incluye casos para números primos, no primos, negativos, ceros, booleanos, decimales, cadenas y otros tipos.

## Ejecución de pruebas

1. Instala pytest si no lo tienes:
   ```
   pip install pytest
   ```

2. Ejecuta las pruebas desde la terminal en la carpeta del proyecto:
   ```
   pytest func_test.py
   ```

## Ejemplo de uso

```python
from func import es_primo

print(es_primo(7))    # True
print(es_primo(10))   # False
print(es_primo(5.5))  # "Error: el parámetro no debe ser decimal"
```

## Autor

- Curso de Inteligencia Artificial -