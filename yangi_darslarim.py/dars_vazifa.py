from os import system
system("cls")


class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Book(Product):
    def __init__(self, id, name, author, count, price):
        super().__init__(id, name)
        self.author = author
        self.count = count
        self.price = price


def faylga_yozish(products, file):
    with open(file, 'w') as f:
        for product in products:
            f.write(f"{product.id},{product.name},{product.author},{product.count},{product.price}\n")


def faylni_uqish(filename):
    products = []
    with open(filename, 'r') as file:
        for line in file:
            product_data = line.strip().split(',')
            id = product_data[0]
            name = product_data[1]
            author = product_data[2]
            count = int(product_data[3])
            price = float(product_data[4])
            book = Book(id, name, author, count, price)
            products.append(book)
    return products


def countni_kamaytirish(products, id):
    for product in products:
        if product.id == id:
            product.count -= 1
            break


def uchirish(products, id):
    for product in products:
        if product.id == id:
            products.remove(product)
            break


book1 = Book("01", "O'tkan kunlar", "Abdulla Qodiriy", 5, 29.99)
book2 = Book("02", "Mehrobdan chayon", "Mehrobdan chayon", 3, 39.99)
book3 = Book("03", "Kecha va kunduz", "Cho'lpon", 7, 19.99)

products = [book1, book2, book3]

faylga_yozish(products, "kitoblar.txt")

read_products = faylni_uqish("kitoblar.txt")

countni_kamaytirish(read_products, "01")

uchirish(read_products, "03")

for product in read_products:
    print(f"Product ID: {product.id}")
    print(f"Name: {product.name}")
    print(f"Author: {product.author}")
    print(f"Count: {product.count}")
    print(f"Price: {product.price}\n")
    print("---------------------------\n")