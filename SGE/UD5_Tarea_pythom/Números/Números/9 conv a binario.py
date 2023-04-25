# Explica que hace el programa
print("""Dame un número y lo combierto en binario""")

# Introdude el número
numero = int(input("> "))

# Convierte a binario
numero_bin = bin(numero)

# Saca los dos primeros caracteres "0b" que es un prefino.
numero_bin_sinpre = numero_bin[2:]

# Mensaje formateado con la funcion de converti a 
mensaje = f"""El número: {numero} en formato "BINARIO" es : {numero_bin_sinpre}
"""

# Imprimir mensaje formateado
print(mensaje)