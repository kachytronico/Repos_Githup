# Explica lo que hace el programa
print("""
Escribe lo que quieras y te diré cuantas veces se repite la letra “a”.
""")
# Pide el texto
cadena = input("> ")

# Cuenta las veces que se repite la "a"
numero_a = cadena.count('a')

# Formatea el mensaje
mensaje = f"""De la frase : {cadena}.

La letra "a" se repite: "{numero_a}"
"""

# Imprime
print(mensaje)
