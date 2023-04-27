print("""
Buenas, para darte respuestas personalizadas, necesito saber un par de datos personales tuyos.
Responde a estas dos preguntas, por favor.
""")

nombre = input("¿Cómo te llamas?  >")

edad = input("¿Qué edad tienes? > ")

mensaje = f"""
Gracias por responder {nombre}.
No quiero parecer grosero pero con {edad} deberías tomarte en serio lo del deporte, comer sano y todo eso que ya sabes.
"""
print(mensaje)