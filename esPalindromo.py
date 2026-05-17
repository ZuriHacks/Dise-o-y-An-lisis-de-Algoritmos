def es_palindromo(X):
    # input: un num entero
    # output: boolean. Verdadero...
    
    if X < 0:
        return False
        
    k = 0
    arr = []
    
    # Bucle para extraer los dígitos y meterlos en el arreglo
    while X > 0:
        digito = X % 10
        arr.append(digito)  # En Python usamos .append() para agregar al arreglo
        k += 1              # Aunque en Python no necesitamos 'k' para indexar, se mantiene la lógica
        X = X // 10         # División entera equivalente a ⌊X/10⌋
        
    # Segunda parte: Verificación de palíndromo usando dos punteros
    n = len(arr)
    i = 0
    j = n - 1
    
    while i <= j:
        if arr[i] != arr[j]:
            return False
        
        i += 1  # Corregido: 'i' avanza hacia la derecha (en la pizarra dice j++)
        j -= 1  # 'j' retrocede hacia la izquierda
        
    return True

print(es_palindromo(121))   # Devuelve: True
print(es_palindromo(-121))  # Devuelve: False (los negativos no son palíndromos)
print(es_palindromo(123))   # Devuelve: False
