import os
os.system("cls")

with open("languages.txt") as f:
    for line in f:
        city, population, country = line.split(",")
        if int(population) > 1000000:
            print(line)