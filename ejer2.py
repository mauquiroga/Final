#Sistema de validación de comentarios Crea un programa que pida al usuario ingresar un comentario sobre un producto
usuario="mau"
comentario="Este es un comentario de prueba"
if "malo" in comentario.lower():
    print("Tu comentario no cumple con las normas, intenta de nuevo.")
else:
    print("Comentario publicado con éxito.")
    print("Gracias por tu comentario,", usuario)
    print("Tu comentario:", comentario)
    print("Comentarios anteriores:")