from instuments import *


class User:
    def __init__(self):
        self.users = []
        self.name = None
        self.surname = None
        self.email = None
        self.password = None
        self.repeatPassword = None

    def fullname(self):
        return '{} {}'.format(self.name, self.surname)

    def add_data(self):
        new_user = []
        controller = False

        self.name = input("name> ")
        self.surname = input("surname> ")
        self.email = input("email> ")

        while not controller:
            self.password = input("password> ")
            self.repeatPassword = input("repeatPassword> ")
            controller = pwd_control(self.password, self.repeatPassword)

            if controller:
                print("Inserimento è andato in buon fine!")

                add_to_file(self.name, self.surname, self.email, self.password)

                new_user.append(self.name)
                new_user.append(self.surname)
                new_user.append(self.email)
                new_user.append(self.password)

                self.users.append(new_user)

                #print(self.users)
            else:
                print("Passwoerd stato errato!")
