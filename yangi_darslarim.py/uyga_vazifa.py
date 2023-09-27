from os import system, path
from math import *
system("clear")




# registratsiya
# login



class Tarmoq:
    def __init__(self):
        self.name = None
        self.username = None
        self.email = None
        self.password = None
        self.choose = [0, 1, 2]
    
    def registration(self):
        self.name = (input("Ismingiz: ")).strip()
        if len(self.name) < 4:
            while len(self.name) < 4:
                self.name = (input("boshqattan urinib ko'ring: ")).strip()

        self.username = (input("Username: ")).strip()
        if len(self.username) < 4:
            while len(self.username) < 4:
                self.username = (input("boshqattan yozib ko'ring username: ")).strip()

        self.email = (input("Emailingizni kiriting: ")).strip()
        if len(self.email) < 4:
            while len(self.email) < 4:
                self.email = (input("boshqattan kiriting emailni: ")).strip()
        self.password = (input("Parolingizni kiriting: ")).strip()
        if len(self.password) < 4:
            while len(self.password) < 4:
                self.password = (input("Boshqattan kiriting parolingizni: ")).strip()
        ind = 1
        if path.exists("users.txt"):
            file = open("users.txt", "r+")
            ind = len(file.readlines()) + 1
            file.write(f"\n{ind}%{self.name}%{self.username}%{self.email}%{self.password}")
            file.close()

        else:
            file = open("users.txt", "a")
            file.write(f"{1}%{self.name}%{self.username}%{self.email}%{self.password}")
            file.close()

        self.clear()

        print("""
            Login [1]
            chiqish [2]
            """)
        tanlov = int(input("select 1 or 2: "))

        if tanlov == 1:
            self.login()
        elif tanlov == 2:
            self.chiqish()
        else:
            exit("Xato tanlov")

    


    def login(self):
        file = (open("users.txt", "r+"))

        ls = file.readlines()
        for i in ls:
            qtor = i.split("%")
            if qtor[3] == self.email:
                self.password = (input("Password: ")).strip()
        if self.password == qtor[4]:
             self.registration()

        

    def kirish(self):
        self.clear()
        print(''' 
            Registratsiya [0]
            Login [1]
            Chiqish [2]
        ''')
        tanlov = int(input("Tanlang: "))
        self.clear()
        if not tanlov in self.choose:
            exit("Xato tanlov")
        if tanlov == self.choose[0]:
            self.registration()
        elif tanlov == self.choose[1]:
            self.login()
        else:
            self.chiqish()

    def chiqish(self):
        exit("Tizimdan chopildik")
    
    def clear(self):
        system("clear")



one = Tarmoq()

one.kirish()