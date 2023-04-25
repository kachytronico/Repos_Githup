# Explica lo que hace el programa
print("Dame dos números y te diré cuál es el mayor")

# Pide un número
numero1 = int(input("> "))

# Pide el otro número
numero2 = int(input("> "))

# Mensajes definidos
mensaje_may = f"""
Para los numeros: {numero1} y {numero2}.

En "MAYOR" el número: {numero1}."""

mensaje_menor = f"""
Para los numeros: {numero1} y {numero2}.

En "MAYOR" el número: {numero2}.
"""

# Compara e imprime los mensajes definidos
if numero1 > numero2:
    print(mensaje_may)
else:
    print(mensaje_menor)