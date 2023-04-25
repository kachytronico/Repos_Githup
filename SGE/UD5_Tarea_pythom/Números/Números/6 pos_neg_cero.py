#Explica lo que hace el programa
print("""
Dame un número y te diré si es "POSITIVO", "NEGATIVO" o "CERO". 
""")

# Pide un número
numero = int(input("> "))

# Mensajes definidos
mensaje_posi = f"""
El número: {numero}. Es "POSITIVO".
"""

mensaje_negativo = f"""
El número: {numero}. Es "NEGATIVO".
"""

# Comparaciones
if numero > 0:
    print(mensaje_posi)
elif numero < 0:
    print(mensaje_negativo)
else:
    print(""""El número introducido es "CERO". """)
