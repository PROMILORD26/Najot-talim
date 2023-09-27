import os
os.system("cls")

import random

# #1-masala...
# class Lyuboy:
#     def __init__(self, kim, nik):
#         self._nik = nik
#         self._kim = kim


#     def get_nik(self):
#         print("helle gays")
        

#     def set_kim(self):
#         print("hello")
        
# n = Lyuboy("hasan", "husen")

# n.get_nik()
# n.set_kim()

#2*-masala...
# class Goool:
#     def __init__(self, cf, gk):
#         self.__cf = cf
#         self.__gk = gk


#     def get_cf(self):
#         return self.__cf 
        

#     def set_gk(self):
#         return self.__gk 
        
# n = Goool("hasan", "husen")

# print(n.get_cf())
# print(n.set_gk())

#3-masala...


# class Benzema:
#     def __init__(self, stiriker, gol_car, scorer):
#         self.__hujumchi = stiriker
#         self.__golm_mashinasi = gol_car
#         self.__gol_muallifi = scorer




class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Noto'g'ri amal! Mablag' yetarli emas.")

    def get_balance(self):
        return self.__balance


    def Acaunt_numbers(self, random_number):
        self.rand_num = random_number
        random.randint(100000,999999)
        return self.rand_num

class Customer:
    def __init__(self, Customer, customer_id, name, email):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__customer = Customer


suka = BankAccount(1234,5000)
print(suka.Acaunt_numbers())