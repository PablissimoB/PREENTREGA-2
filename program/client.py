from datetime import datetime

class Client:

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.date_creation = datetime.now()
        self.id = self.__str__()

    def __str__(self):
        return self.email+"_"+str(int(self.date_creation.strftime("%Y%m%d%H%M%S")))

    def print_client(self):
        print(f"Id: {self.id}")
        print(f"Nombre: {self.first_name}")
        print(f"Apellido: {self.last_name}")
        print(f"Mail: {self.email}")
        print(f"Teléfono: {self.password}")
        print(f"Creación: {self.date_creation}")
    
    