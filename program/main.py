from client import Client

database =[]
continuar = False

def post_data():
    print("----CREAR OBJETO----" )
    first_name = input("Ingrese el nombre: ")
    last_name = input("Ingrese el apellido: ")
    email = input("Ingrese el email: ")
    password = input("Ingrese el password: ")
    if first_name =="" or last_name=="" or email=="" or password =="" :
        print("no ha ingresado datos")
    else:
        email = Client(
            first_name,
            last_name,
            email,
            password
        )
        database.append(email)

def get_all_data(myDatabase):
    print("----CONSULTAR TODOS LOS OBJETOS----" )
    for objeto in myDatabase:
        objeto.print_client()
        print("------------------" )
    print("------------------" )
    return False

def log_user(myDatabase):
        print("----LOGIN----" )
        mail = input("Ingrese el mail: ")
        password = input("Ingrese el password: ")
        contrasena = None
        for objeto in myDatabase:
            if objeto.email == mail:
                contrasena = objeto.password
        if contrasena == password:
            print("bienvenido")
            return True
        else :
            print("Usuario o Password incorrecto")
            return False

def get_data(myDatabase):
    print("----CONSULTAR OBJETO----" )
    mail = input("Ingrese el email a consultar: ")
    for objeto in myDatabase:
        if objeto.email == mail:
            objeto.print_client()
    print("------------------" )
    return False

def myPanel():
    print("-------MENU-------" )
    print("Elija la opción:")
    print("1-Ingresar datos")
    print("2-Consultar todos los datos")
    print("3-Login")
    print("4-Buscar y consultar usuario")
    print("0-Salir")
    opcion = input()
    if opcion == "1":
        post_data()
        return False
    elif opcion == "2":
        get_all_data(database)
        return False
    elif opcion == "3":
        return log_user(database)
    elif opcion == "4":
        return get_data(database)
    elif opcion == "0":
        return True
    else:
        print("Opcion incorrecta")
        return False

def myProgram(panel): 
    while panel != True:
        panel = myPanel()
        
myProgram(continuar)
