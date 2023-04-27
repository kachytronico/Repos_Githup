print("""

Escribe un número y te diré si es "PAR o IMPAR"

NO TE LO CREES... ¡¡ pues ponme a prueba!!
""")

# convierte el número a un entero (int), después de entrarlo con (input)
n1 = int(input("Ingresa el número> "))

# Utilizamos el operador (%) para saber su resto y si es igual (==) a 0 imprime
if n1 % 2 == 0:
    print("El número: ", n1, " Es PAR")
else:
    print("El número: ", n1, " Es IMPAR")



