users  = {}
status = ""

def displayMenu():
    status = input("Are you registrated user? y/n? Press q to quit")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()

def newUser():
    createLogin = input("Create login name: ")
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createemail = input("write your email:")
        wgps = input("write adres: ")
        createPassw = input("create password: ")
        users[createLogin] = wgps         
        users[createLogin] = createPassw   
        users[createLogin] = createemail 
        print("\nUser created\n")

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        print("\nLogin ")
    else:
        print("\nUser doesen't exist or wrong password!\n")

while status != "q":
    displayMenu()
    

    
