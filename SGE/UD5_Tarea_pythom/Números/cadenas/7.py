# Explica lo que hace el programa
print("""
Escribe lo que quieras y  te diré la “Primera” y la “Última” letra que escribas.
""")
# Pide el texto
cadena = input("> ")

# Saca la primera
primera = cadena[0]

# Saca la última
ultima = cadena[-1]

# Formatea el mensaje
mensaje = f""" De la frase : {cadena}.

La primera letra es: "{primera}"

Y la última letra es: "{ultima}" """

# Imprime
print(mensaje)