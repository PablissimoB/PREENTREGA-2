from client import Client

database ={}
continuar = False

def post_data(myDatabase):
    print("----INGRESAR----" )
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

def get_all_data():
    print("----CONSULTAR----" )
    print("------------------" )
    return False

def log_user(myDatabase):
        print("----LOGIN----" )
        mail = input("Ingrese el mail: ")
        password = input("Ingrese el password: ")
        contrasena = myDatabase.get(mail)
        if contrasena == password:
            print("bienvenido")
            return True
        else :
            print("Usuario o Password incorrecto")
            return False

def get_data():
    print("----CONSULTAR----" )
    mail = input("Ingrese el email a consultar: ")
    print("------------------" )
    return False

def myPanel(myDatabase):
    print("-------MENU-------" )
    print("Elija la opción:")
    print("1-Ingresar datos")
    print("2-Consultar todos los datos")
    print("3-Login")
    print("4-Buscar y consultar usuario")
    print("0-Salir")
    opcion = input()
    if opcion == "1":
        post_data(myDatabase)
        return False
    elif opcion == "2":
        get_all_data(myDatabase)
        return False
    elif opcion == "3":
        return log_user(myDatabase)
    elif opcion == "4":
        return get_data()
    elif opcion == "0":
        return True
    else:
        print("Opcion incorrecta")
        return False

def myProgram(panel): 
    while panel != True:
        panel = myPanel(database)
        
myProgram(continuar)
