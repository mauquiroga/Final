usuario=mau
contra=123
if usuario=="mau" and contra=="123":
    print("Acceso concedido")
else:
    print("Acceso denegado")
    print("Intente nuevamente.")
    usuario=input("Ingrese su nombre de usuario: ")
    contra=input("Ingrese su contraseña: ")
    if usuario=="mau" and contra=="123":
        print("Acceso concedido")
        
