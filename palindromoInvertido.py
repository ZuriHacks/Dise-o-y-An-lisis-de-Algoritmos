def es_palindromo(X):
    # i: un número entero
    # o: boolean. Verdadero si es palíndromo, Falso si no.
    
    if X < 0:
        return False
        
    invertido = 0
    original = X
    
    while X > 0:
        digito = X % 10
        invertido = (invertido * 10) + digito
        X = X // 10  # División entera en Python equivalente a ⌊X / 10⌋
        
    return original == invertido

# --- Ejemplos de prueba para verificar ---
print(es_palindromo(121))   # Devuelve: True
print(es_palindromo(12321)) # Devuelve: True
print(es_palindromo(456))   # Devuelve: False
print(es_palindromo(-121))  # Devuelve: False
