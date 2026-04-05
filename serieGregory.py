n_total = int(input("Ingresa el número de términos (n): "))

cadena_serie = ""

for i in range(1, n_total + 1):
    # k es el índice que empieza en 0 para la fórmula (2k + 1)
    k = i - 1
    denominador = 2 * k + 1
    
    # Lógica para construir la cadena tal como en la imagen
    if k == 0:
        cadena_serie += "4"
    elif k % 2 == 0:
        # Si es par, se suma
        cadena_serie += f" + 4/{denominador}"
    else:
        # Si es impar, se resta
        cadena_serie += f" - 4/{denominador}"
        
    # Imprime el resultado con el formato exacto del pizarrón
    print(f"n={i} | {cadena_serie}")