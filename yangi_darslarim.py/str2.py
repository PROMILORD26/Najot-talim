# import os
# os.system("cls")
# n = int(input('n ga qiymat bering :) '))

# str = input('satrni kiriting :) ')
# str = str.split(' ')
# creat = True
# if n > len(str):
#     while creat:
#         str.append('.')
#         if n == len(str):
#             creat = False
# elif n < len(str):
#     while creat:
#         str.append('.')
#         str.pop()
#         if n == len(str):
#             creat = False

# print(n)
# print(str)
# print(len(str))     




# # class Komanda:
# #     def jamoa(self):
# #         pass 

# # class Futbol(Komanda):
# #     def jamoa(self):
# #         print("Futbolchilar jamoasi")    


# # class Voleybol(Komanda):
# #     def jamoa(self):
# #         print("Valebolchilar jamoasi")

# # class Basketbol(Komanda):
# #     def jamoa(self):
# #         print("Basketbolchilar jamoasi")
                

# # class Futzal(Komanda):
# #     def jamoa(self):
# #         print("Futzalchilar jamoasi")

# # futbol = Futbol()
# # futbol.jamoa()

# # volebol = Voleybol()
# # volebol.jamoa()

# # basketbol = Basketbol()
# # basketbol.jamoa()

# # futzal = Futzal()
# # futzal.jamoa()




# # class Human:
# #     def tepish(self, tepish, yugurish):
# #         self.tepish = tepish
# #         self.yugurish = yugurish
    
# #     def tepish(self):
# #         return self.tepish
# #         print("inson tepdi")
    
# #     def yugurish(self):
# #         return self.yugurish
        


# # class Koptok:
# #     def toppi(self, uchish, dumalash):
# #         self.uchish = uchish
# #         self.dumalash = dumalash


# #     def uchish(self):
# #         return self.uchish
# #         print("koptok uchdi")    


# # koptok = Koptok()


# class Kitob:
#    def __init__(self, kitob_nomi, kitob_muallifi, kitob_narxi, kitob_nashriyoti):
#       self.nomi = kitob_nomi
#       self.muallif = kitob_muallifi
#       self.narxi = kitob_narxi
#       self.nashriyoti= kitob_nashriyoti
       
#    def nomii(self):
#       return self.nomi

#    def mualliff(self):
#       return self.muallif

#    def narxii(self):
#       return self.narxi

#    def nashriyott(self): 
#       return self.nashriyoti

# nomi = input("Kitob nomini kiriting: ")
# muallif = input("Kitob muallifini kiriting: ")
# narxi = int(input("Kitob narxini kiriting: "))
# nashriyot = input("Kitob nashriyotini kiriting: ")
# book = Kitob(nomi, muallif, narxi, nashriyot)

# print()
# print(f"Kitob nomi: {book.nomii()}\nkitob muallif: {book.mualliff()}\nkitob narxi: {book.narxii()} ming so'm\nkitob nashriyoti: {book.nashriyott()}")


# 1-masala...
# class Hazon:
#     pass

#####################################################################
# 2-masala...
# class Kuz:
#     def __init__(self):
        # pass

################################################################
# 3-amsala...
# class Kuz:
#     def __init__(self, hazon):
#         pass

##################################################################
# 4-masala...
# class Hazon:
#     @classmethod
#     def show(cls):
#         print("salom")
# print()
# Hazon.show()  

###################################################################
# 5-masala...
# class Animal:
#     def __init__(self, kiyik, quyon):
#         self.kiyik = kiyik
#         self.qoyon = quyon
#     def quyonchik(self):
#         return self.qoyon
    
#     def kiyikjon(self):
#         return self.kiyik

##################################################################
# 6-masala...
# class Futbol:
#     def __init__(self, nomi, qayerdan, klubi, yoshi, raqami, maosh, ):
#         self.name = nomi
#         self.country = qayerdan
#         self.club = klubi
#         self.nomer = raqami

#     def futbolchi_ismi(self):
#         return self.name
    
#     def futbolchi_vatani(self):
#         return self.country
    
#     def futbolchi_clubi(self):
#         return self.club
    
#     def futbolchi_raqami(self):
#         return self.nomer
    
#     def futbolchi_ismi(self):
#         return self.name

##################################################################
# 7-masala...
# class Car: 
#     def __init__(self,name, year, speed):
#         self.ism = name 
#         self.yil = year 
#         self.tezlik = speed
    
#     def name(self):
#         return self.ism
    
#     def year(self):
#         return self.yil
    
#     def speed(self):
#         return self.tezlik
    
#     def  start(self):
#         return f"o't olish"
    
#     def  stop(self):
#         return f"to'xtab turish"
    
#     def  turn_right(self):
#         return f"o'ng tomonga burilish"   

#     def turn_back(self):
#         return f"orqaga yurish"
    

# avto = Car("AUDI", "2018", "320")
# avto2 = Car("BMW", "2019", "350")
# avto3 = Car("NISSAN", "2012", "420")
# avto4 = Car("FORD", "2020", "390")
# avto5 = Car("LAMBORGHINI", "2022", "480")

# print(f"AVTO nomi:{avto.ism},\n AVTO yili:{avto.yil},\n AVTO tezligi:{avto.tezlik},")

###########################################
# 8-masala...
# class Talaba:
#     def __init__(self, ism, familiya, baho):
#         self.name = ism
#         self.surname = familiya
#         self.betting = baho
    
# class Talaba_bola(Talaba):
#     def baholash(self):
#         if self.betting <= 5:
#             print("alochi")

#         elif self.betting >= 4:
#             print("yaxshi")

#         elif self.betting >=3:
#             print("qoniqarli")

#         elif self.betting >=2:
#             print("qoniqarsiz")

#         elif self.betting >=1:
#             print("yomon") 
# bola = Talaba_bola("Hasan", "Pulatov", 2) 
#ustoz bu chala bup qoldi...

####################################################################
# 9-masala...
# class Human:
#     def __init__(self, name, age, profession, height, weight,single):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.height = height
#         self.weight = weight
#         self.single = single

#     def get_name(self):
#         return self.name   
#     def get_age(self):
#         return self.age
#     def get_profession(self):
#         return self.profession
#     def get_height(self):
#         return self.height
#     def get_weight(self):
#         return self.weight
#     def get_single(self):
#         return self.single
    
# person = Human("Hasan", 22, "programming", 1.90, 75, "solitary")

# print(f"PERSON->{person.get_name} >>> AGR->{person.get_age} >>> PROFESSION->{person.get_profession} >>> HEIGHT->{person.get_height} >>> WEIGHT->{person.get_weight} >>> SINGLE->{person.get_single} >>>")