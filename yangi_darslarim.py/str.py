import os
os.system("cls")

# 1-masala...
# nom = 'salom'
# print(nom[0],nom[2],nom[-1])
############################################################################
#2-masala...
# nom = 'salom'
# print(nom[1:4])
############################################################################
# 3-masala...
# nom = 'salom'
# soz = nom[:3] + 'alik' + nom[3:]
# print(soz)
###########################################################################
# 4-masala...
# nom = input("so'z kiriting: ")
# nom1 = input("so'z kiriting: ")
# nom2 = input("so'z kiriting: ")
# nom3 = input("so'z kiriting: ")

# soz = nom[0] + nom1[0] + nom2[0] + nom3[0]
# print(soz)
########################################################################
# 5-masala...
# nom = 'Hasanjon'
# print(nom[::-1])
#########################################################################
# 6-masala...
# nom = 'String slicing in Python'
# print('a)', nom[13:17])
# print('b)',nom[-2])
# print('c)', nom[4], nom[-1])
# print('d)', nom[7:-1])
# print('e)', nom[-6] + nom[-1], '  ', nom[4] + nom[10] + nom[8])
# print('f)', nom[0] + nom[3])
# print('g)',nom[-5:])
# print('h)', nom[-6])
# # print('i)', nom[])ustoz buni qilishga erindim
# print('j)', nom[2] + nom[5] + nom[8:10])
############################################################################
# 7-masala..
# a = input("so'z kiriting: ")
# n = int(input("belgini kiriting: "))
# print(a[0:n])
##########################################################################
# 8-masala...
# a = input("so'z kiriting: ")
# n = int(input("belgini kiriting: "))
# print(a[n::-1])
########################################################################
# 9-masala...
# n = "hasan"
# a = n[2:]
# print(a[::-1])
#########################################################################
# 10-masala...
# n = input("so'zni kiriting: ")
# for n in len(n):
#     print(n)        





# # TO"G"RI VARIATI
# import os
# os.system("cls")


# sozni o'rtasidagi belgini olish 
# a="This is called Python"
# a[len(a)//2]  #shu o'rtasid'agi belgini oladi.
# 
# 
# yoki bitta o'zgaruvchiga o'rtasidagi indexni olib olish mumkun
# 
# middle= len(a)//2
# 
# print(a[middle]) 
# 
#  




# 1-masala...
# nom = 'salom'
# print(nom[0],nom[2],nom[-1])

############################################################################

#2-masala...
# nom = 'salom'
# print(nom[1:4])

############################################################################

# 3-masala...
# nom = 'salom'
# soz = nom[:3] + 'alik' + nom[3:]
# print(soz)

###########################################################################

# 4-masala...
# nom = input("so'z kiriting: ")
# nom1 = input("so'z kiriting:' ")
# nom2 = input("so'z kiriting: ")
# nom3 = input("so'z kiriting: ")

# har bitta so'zni boshi o'rtasi oxiri dagi belgilarni olishiz kerak edi

# soz = nom[0] + nom[len(nom)//2] + nom[-1] + nom1[0] + nom1[len(nom1)//2] + nom1[-1] + nom2[0] + nom2[len(nom2)//2] + nom2[-1] + nom3[0] + nom3[len(nom3)//2] + nom3[-1]
# print(soz)

########################################################################

# 5-masala...
# nom = 'Hasanjon'
# print(nom[::-1])

#########################################################################

# 6-masala...
# nom = 'String slicing in Python'
# print('a)', nom[13:17])
# print('b)',nom[-2])
# print('c)', nom[4], nom[-1])
# print('d)', nom[7:-1])
# print('e)', nom[-6] + nom[-1], '  ', nom[4] + nom[10] + nom[8])
# print('f)', nom[0] + nom[3])
# print('g)',nom[-5:])
# print('h)', nom[-6])
# # print('i)', nom[])ustoz buni qilishga erindim  i gnicilS gnirt --> tring Slicing i  nom[1:16:-1] qilsez chiqardi.
# print('j)', nom[2] + nom[5] + nom[8:10])

############################################################################

# 7-masala..
# a = input("so'z kiriting: ")
# n = int(input("belgini kiriting: "))
# print(a[0:n])
##########################################################################

# o'ng tarafdagi n ta belgi chiqishi kerak edi

# a = This is python n=5  natija ython  a[-n:]

# 8-masala...
# a = input("so'z kiriting: ")
# n = int(input("belgini kiriting: "))
# print(a[n::-1])

########################################################################
# 9-masala...
# n = "hasan"
# a = n[2:]
# print(a[::-1])
#########################################################################
# 10-masala...
# n = input("so'zni kiriting: ")

# # uzunligini juft yoki toqlikka tekshirish
# if len(n) % 2 == 0:
#     #juft indexdagi harflarni chiqarish
#     for i in range(0,len(n),2): # range(0,len(n),2)  --> [0,2,4,6,8,10,....] n gacha juft sonlardan iborat list qaytaradi.
#         print(n[i])        
# else:
#     for i in range(1,len(n),2): # range(1,len(n),2)  --> [1,3,5,7,9,....] n gacha toq sonlardan iborat list qaytaradi.
#         print(n[i])        