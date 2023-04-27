# Explica lo que hace el programa
print("Dame un número y te diré si es un número perfecto")
# Es perfecto si la suma de sus dibisores es igual a este


# Para saber si un número es perfecto debemos saber:
##### Los divisores propios de un número son los divisores positivos menores que este.
##### Será perfecto si la suma de sus divisores propios es igual al este.

# Pide un número
numero_a_comprobar = int(input("> "))

# define divisor menor y total
divisor = 1
total = 0

# bucle para comprobar que los divisores menores son
while (divisor < numero_a_comprobar):
    # Compara se el resto de cada división es igual a "0"
    if numero_a_comprobar % divisor == 0:
        # Acomulador
        total = total + divisor
    # Contador para que no sea un bucle infinito
    divisor = divisor + 1

# Comparar si es igual al número introducido
if total == numero_a_comprobar:
    print("""Es un número "PERFECTO".""")
else:
    print(""" No es "PERFECTO". """)