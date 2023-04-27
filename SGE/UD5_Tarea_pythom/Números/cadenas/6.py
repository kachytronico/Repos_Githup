# Explica lo que hace el programa
print("""
Escribe lo que quieras y te diré si la longitud de lo que escribes es "IMPAR" o "PAR"
""")
      
# Pide el texto
cadena = input("> ")

# Mide la longitud
longitud = len(cadena)

# La divide entre 2
resultado = longitud % 2

# Comprueba si es PAR y lo imprime
if resultado == 0:
    print("Es PAR")

# Sino es par lo imprime
else:
    print("Es IMPAR")