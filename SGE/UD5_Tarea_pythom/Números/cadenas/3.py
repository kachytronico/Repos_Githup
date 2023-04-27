# Explica lo que hace el programa
print(""" Escribe una frase y le daré la vuelta
""")

# Pide la frase
cadena = input(" >")

# Define la cadena invertida vacía
cadenaInvertida = ""

# Recorremos la cadena letra a letra y la guardamos al principio de la cadena para que la invierta
for letra in cadena:
    cadenaInvertida = letra + cadenaInvertida

print(cadenaInvertida)