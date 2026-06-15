#Filtro de seguridad (While + If) Crea un sistema que pida una contraseña al usuario
contrasena_correcta = "1234"
while True:
    contrasena = input("Ingrese la contraseña: ")
    if contrasena == contrasena_correcta:
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta, intente nuevamente.")
        
