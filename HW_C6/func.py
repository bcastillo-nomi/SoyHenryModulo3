def es_primo(num):
    """Check if a number is prime."""
    # Validar tipo de dato
    if isinstance(num, bool):
        return "Error: el parámetro no debe ser booleano"
    if isinstance(num, float):
        return "Error: el parámetro no debe ser decimal"
    if isinstance(num, str):
        return "Error: el parámetro no debe ser una cadena"
    if not isinstance(num, int):
        return "Error: el parámetro debe ser un número entero"
    if num < 2:
        return False  # 0 y 1 no son primos, tampoco negativos

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(es_primo(5))
