# Explica lo que hace el programa
print("""
Escribe lo que quieras y te diré si contiene la palabra "python"
""")

# Pide el texto
cadena = input("> ")

# Lo busca i imprime si está
if 'python' in cadena:
    print("Si está")

# Sino esta lo imprime
else:
    print("No está")