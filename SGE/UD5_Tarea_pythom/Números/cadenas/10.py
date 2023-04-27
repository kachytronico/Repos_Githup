# Explica lo que hace el programa
print("""
Escribe lo que quieras y te diré si es un palíndromo
""")
      
# Pide el texto
cadena = input("> ")

# Da la vuelta a la cadena
cadenainvertida = cadena[::-1]

# comparar las dos variables
if cadena == cadenainvertida:
    print(f""" Pues, puedo confirmar que "{cadena}", si es un palíndromo""")
else:
    print(f""" Pues, puedo confirmar que "{cadena}", no es un palíndromo""")