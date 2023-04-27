# Explica lo que hace el programa
print("Dame tres números y te diré cuál es el menor")

# Pide primer número
numero1 = int(input("Pon el primer número> "))

# Pide el segundo número
numero2 = int(input("Pon el segundo número> "))

# Pide el trecer número
numero3 = int(input("Pon el tercer número> "))

# Mensajes definidos
mensaje_menor1 = f"""
Para los números: {numero1}, {numero2} y {numero3}.

El "MENOR" de ellos es el número: {numero1}."""

mensaje_menor2 = f"""
Para los números: {numero1}, {numero2} y {numero3}.

El "MENOR" es el número: {numero2}.
"""

mensaje_menor3 = f"""
Para los números: {numero1}, {numero2} y {numero3}.

El "MENOR" es el número: {numero3}.
"""

# Compara e imprime los mensajes definidos
if numero1 <= numero2 and numero1 <= numero3:
    print(mensaje_menor1)
elif numero2 < numero1 and numero2 < numero3:
    print(mensaje_menor2)
else:
    print(mensaje_menor3)