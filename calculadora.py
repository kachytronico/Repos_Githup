# Explicar lo que hace el código
print("""
------ CALCULADORA -----
""")


# Define la FUNCIÓN que muestra un menú de opciones




def mostrar_menu_opciones():
    print("""Estas son las opciones y debes elegir una:


    1- SUMAR dos números.
    2- RESTAR dos números.
    3- MULTIPLICAR dos números.
    4- DIVIDIR dos números.


    0- SALIR del programa.
    """)


# Define la FUNCIÓN de la operación




def operar(operacion):
    n1 = int(input("Introduce un valor> "))
    n2 = int(input("Introduce otro valor> "))
    if operacion == 1:
        resultado = n1 + n2
    elif operacion == 2:
        resultado = n1 - n2
    elif operacion == 3:
        resultado = n1 * n2
    elif operacion == 4:
        resultado = n1 / n2
    return resultado




# Empieza el programa mostrando el menú
mostrar_menu_opciones()


# Pide la opción al usuario
opcion = int(input("¿Qué quieres hacer? >"))


# Bucle con las opciones y sus operaciones
while (opcion) < 5:
    # Sale del bucle si la opción es "0"
    if opcion == 0:
        break


    # SUMA
    elif opcion == 1:
        print("""
        Vamos a sumar
        """)
        resultado_suma = operar(opcion)
        print(f"""
        El resultado de la suma es: {resultado_suma}
        """)


    # RESTA
    elif opcion == 2:
        print("""
        Vamos a restar
        """)
        resultado_resta = operar(opcion)
        print(f"""
        El resultado de la resta es: {resultado_resta}
        """)


    # MULTIPICAR
    elif opcion == 3:
        print("""
        Vamos a multiplicar
        """)
        resultado_multiplicar = operar(opcion)
        print(f"""
        El resultado de la multiplicación es: {resultado_multiplicar}
        """)


    # DIVIDIR
    elif opcion == 4:
        print("""
        Vamos a dividir
        """)
        resultado_dividir = operar(opcion)
        print(f"""
        El resultado de la división es: {resultado_dividir}
        """)


    # Opción no válida
    else:
        print("""
        No has marcado una opción válida.
        """)


    # Muestar el menú de nuevo y pide la opción
    mostrar_menu_opciones()
    opcion = int(input("""
    ¿Qué quieres hacer? >
    """))


# Termina el programa
print("""
FIN DEL PROGRAMA
""")
