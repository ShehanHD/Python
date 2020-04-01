from user import Register, Login

arr = ("Nome", "Cognome", "e-mail", "Password", "Ripeti Password")
x = 1

register = Register(arr)
login = Login(arr)

while (x != 0):
    x = int(input("\n1 per aggiungere nuova utente\n2 per Login\n0 per uscire\n> "))

    if x == 1:
        register.add_user(arr)
    elif x == 2:
        login.control_login();
    else:
        pass
        #print("inserimennto sbagliato")

