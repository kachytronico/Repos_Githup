# Explica lo que hace el programa
print("""
Escribe lo que quieras y te diré la longitud de lo que escribas
""")

# Pide el texto
cadena = input("> ")

# Mide la longitud
numero_caracteres_cadena = len(cadena)

# Formatea el mensaje
mensaje = f"""La frase : {cadena}.

Tiene una longitud de: "{numero_caracteres_cadena}"
"""

# Imprime
print(mensaje)
