
print("""Ahora si me das un número te enseño cómo es su tabla de multiplicar del 1 hasta el 10""")

n1 = input("ingresa el número >")

n1 = int(n1)

m1 = n1 * 1
m2 = n1 * 2
m3 = n1 * 3
m4 = n1 * 4
m5 = n1 * 5
m6 = n1 * 6
m7 = n1 * 7
m8 = n1 * 8
m9 = n1 * 9
m10 = n1 * 10

mensaje = f"""
Para el número {n1},
el resultado de la multiplicación es:
{n1} x 1 = {m1}
{n1} x 2 = {m2}
{n1} x 3 = {m3}
{n1} x 4 = {m4}
{n1} x 5 = {m5}
{n1} x 6 = {m6}
{n1} x 7 = {m7}
{n1} x 8 = {m8}
{n1} x 9 = {m9}
{n1} x 10 = {m10}

"""

print(mensaje)
