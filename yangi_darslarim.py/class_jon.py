# class Book:
#     def __init__(self,name, count_pages, price): # __init__ = Konstruktor
#         self.book_name = name                    # self.book_name => attribute, property
#         self.book_count_pages = count_pages
#         self.book_price = price

# book1 = Book("Graf Monte Cristo",1665,150000)    # book1  => obyekt
# book2 = Book("Graf Monte Cristo 1",1365,140000)  # book2  => obyekt
# book3 = Book("Graf Monte Cristo 2",1165,120000)  # book3  => obyekt
# book4 = Book("Graf Monte Cristo 3",965,110000)   # book4  => obyekt
# book5 = Book("Graf Monte Cristo programming 4",665,50000)    # book5  => obyekt

# ls = [book1,book2,book3,book4,book5] 
# sum1  = 0
# narx = 0
# for i in ls:
#     sum1 += i.book_count_pages
#     narx += i.book_price

# umumiy = narx // sum1 

# print("bitta varoq narxi:", umumiy, "so'm ekan janoblar")

# for i in ls:
#     if  'programming' in i.book_name : 
#         i.book_price *= 2
#         print("programming qatnashgan so'zlar:", i.book_price)       


# class Person :
#     def __init__(self, first_name, last_name,  birthdate):
#         self.man_first_name = first_name
#         self.man_Last_name = last_name
#         self.man_birthdate = birthdate

#     def get_info():
#         pass


# class Student(Person):
#     def __init__(self, first_name, last_name, birthdate, faculty, level):
#         super().__init__(first_name, last_name, birthdate)
#     def get_info(self):
#         pass
# # chala...



# class Player:
#     def __init__(self, name, health) -> None:
#         self.name = name
#         self.health = health

#     def attack(self, object):
#         object.health -= 10
#         return f"pichladi s**a !!!"

# class Terrors(Player):
#     def __init__(self, name, health, money) -> None:
#         super().__init__(name, health)
#         self.money = money
#     def attack(self, object):
#         if not isinstance(object, Terrors):
#             object.health -= 20


# class CounterTerrors(Player):
#     def __init__(self, name, health, money) -> None:
#         super().__init__(name, health)
#         self.money = money
#         if not isinstance(object, Terrors):
#             object.health -= 20


# class Gun:
#     def __init__(self, gun_name, gun_price, damage) -> None:
#         self.name_gun = gun_name
#         self.price_gun = gun_price
#         self.damage_gun = damage

# qurol = Gun("AK-47", 30000, 30)
# qurol2 = Gun("M4", 25000, 26)
# qurol3 = Gun("AK117", 29000, 33)
# qurol4 = Gun("KN-44", 25000, 25)
# qurol5 = Gun("M13", 20000, 22)




