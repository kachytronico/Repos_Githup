# Para ser un número "PRIMO". Este número tiene que ser divisible sólo entre sí mismo y el 1
# El resto de cualquier otra división no puede ser "CERO"

# Explica lo que hace el programa
print("Dame un número y te diré si es primo o no")

# Pide un número
numero_a_comprobar = int(input("> "))

# Definir número para dividir
numero_para_div = numero_a_comprobar - 1

# Define es primo para imprimir al salir del while
primo = True

# Cambiar primo a "FALSE" si el número a comprobar es "uno" porque no cumple la regla.
if numero_a_comprobar == 1:
    primo = False

# Mientas el número a dividir sea mayor que "1", dividir y sacar el resto.
while numero_para_div > 1:
    # Dividir y sacar el resto.
    resto = numero_a_comprobar % numero_para_div
    numero_para_div -= 1

    # Si el resto es "CERO" parar porque "NO" es primo
    if resto == 0:
        primo = False
        break

# Comprobar si primo sigue siendo true e imprimir
if primo == True:
    print("Es primo")
else:
    print("No es primo")
