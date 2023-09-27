import random
e="✌️","✊","✋"
n="\n"
b="Yutdingiz"
c="Yutqazdingiz"
def f():
 x=random.choice(e)
 a=x+n
 y=input("qaychi,qog'oz,quduq: ")
 if x==e[0] and y=="quduq":
  print(a+e[1]+n+b)
  f()
 elif x==e[0] and y=="qog'oz":
  print(a+e[2]+n+c)
  f()
 elif x==e[1] and y=="qaychi":
  print(a+e[0]+n+c)
  f()
 elif x==e[1] and y=="qog'oz":
  print(a+e[2]+n+b)
  f()
 elif x==e[2] and y=="qaychi":
  print(a+e[0]+n+b)
  f()
 elif x==e[2] and y=="quduq":
  print(a+e[1]+n+c)
  f()
 else:
  print("Durrang")
  f()
f()