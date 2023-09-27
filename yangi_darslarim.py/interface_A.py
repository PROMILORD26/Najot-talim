
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtBoundSignal
from PyQt5.QtWidgets import *
import sys
from os import system

system("clear")


class Dastur(QMainWindow):
    def __init__(self):
        super(Dastur, self).__init__()
        self.setWindowTitle("Iphone 15 Pro Max")
        self.resize(360, 670)
        self.move(1455, 30)
        self.setStyleSheet("""background-color: black;""")

        self.expression = ""

        ac = QPushButton("AC", self)
        ac.setGeometry(25, 260, 70, 70)
        ac.setFont(QFont("Calibri", 50))
        ac.setStyleSheet("""background-color : rgb(147, 145, 141);
                        color: azure;
                        border-radius : 35px;""")
        ac.clicked.connect(self.clear_expression)

        ishora = QPushButton("+/-", self)
        ishora.setGeometry(105, 260, 70, 70)
        ishora.setStyleSheet("""background-color : rgb(147, 145, 141);
                        color: azure;
                        border-radius : 35px;""")
        ishora.clicked.connect(self.toggle_sign)

        foiz = QPushButton("%", self)
        foiz.setGeometry(185, 260, 70, 70)
        foiz.setStyleSheet("""background-color : rgb(147, 145, 141);
                            color: azure;
                            border-radius : 35px;""")
        foiz.clicked.connect(self.calculate_percentage)

        bolish = QPushButton("/", self)
        bolish.setGeometry(265, 260, 70, 70)
        bolish.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")
        bolish.clicked.connect(lambda: self.append_operator("/"))

        yetti = QPushButton("7", self)
        yetti.setGeometry(25, 340, 70, 70)
        yetti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        yetti.clicked.connect(lambda: self.append_number("7"))

        sakiz = QPushButton("8", self)
        sakiz.setGeometry(105, 340, 70, 70)
        sakiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        sakiz.clicked.connect(lambda: self.append_number("8"))

        toqqiz = QPushButton("9", self)
        toqqiz.setGeometry(185, 340, 70, 70)
        toqqiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        toqqiz.clicked.connect(lambda: self.append_number("9"))

        kopaytirma = QPushButton("x", self)
        kopaytirma.setGeometry(265, 340, 70, 70)
        kopaytirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")
        kopaytirma.clicked.connect(lambda: self.append_operator("*"))

        tort = QPushButton("4", self)
        tort.setGeometry(25, 415, 70, 70)
        tort.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        tort.clicked.connect(lambda: self.append_number("4"))

        besh = QPushButton("5", self)
        besh.setGeometry(105, 415, 70, 70)
        besh.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        besh.clicked.connect(lambda: self.append_number("5"))

        olti = QPushButton("6", self)
        olti.setGeometry(185, 415, 70, 70)
        olti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        olti.clicked.connect(lambda: self.append_number("6"))



        ayirma = QPushButton("-", self)
        ayirma.setGeometry(265, 415, 70, 70)
        ayirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")
        ayirma.clicked.connect(lambda: self.append_operator("-"))

        bir = QPushButton("1", self)
        bir.setGeometry(25, 490, 70, 70)
        bir.setStyleSheet("""background-color : rgb(continued)""")

        bir.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        bir.clicked.connect(lambda: self.append_number("1"))

        ikki = QPushButton("2", self)
        ikki.setGeometry(105, 490, 70, 70)
        ikki.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        ikki.clicked.connect(lambda: self.append_number("2"))

        uch = QPushButton("3", self)
        uch.setGeometry(185, 490, 70, 70)
        uch.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        uch.clicked.connect(lambda: self.append_number("3"))

        qoshish = QPushButton("+", self)
        qoshish.setGeometry(265, 490, 70, 70)
        qoshish.setStyleSheet("""background-color : rgb(208, 137, 13);
                                color: azure;
                                border-radius : 35px;""")
        qoshish.clicked.connect(lambda: self.append_operator("+"))

        nol = QPushButton("0          ", self)
        nol.setGeometry(25, 565, 150, 70)
        nol.setStyleSheet("""background-color : rgb(58, 57, 55);
                                color: azure;
                                border-radius : 35px;""")
        nol.clicked.connect(lambda: self.append_number("0"))

        nuqta = QPushButton(".", self)
        nuqta.setGeometry(185, 565, 70, 70)
        nuqta.setStyleSheet("""background-color : rgb(58, 57, 55);
                                color: azure;
                                border-radius : 35px;""")
        nuqta.clicked.connect(lambda: self.append_decimal())

        teng = QPushButton("=", self)
        teng.setGeometry(265, 565, 70, 70)
        teng.setStyleSheet("""background-color : rgb(208, 137, 13);
                                color: azure;
                                border-radius : 35px;""")
        teng.clicked.connect(self.calculate_result)

    def append_number(self, number):
        self.expression += number

    def append_operator(self, operator):
        self.expression += operator

    def append_decimal(self):
        if self.expression and self.expression[-1].isdigit():
            self.expression += "."

    def clear_expression(self):
        self.expression = ""

    def toggle_sign(self):
        if self.expression and self.expression[-1].isdigit():
            last_number = self.get_last_number()
            if last_number.startswith("-"):
                self.expression = self.expression[:-len(last_number)] + last_number[1:]
            else:
                self.expression = self.expression[:-len(last_number)] + "-" + last_number

    def calculate_percentage(self):
        last_number = self.get_last_number()
        if last_number and last_number.isdigit():
            percentage = float(last_number) / 100
            self.expression = self.expression[:-len(last_number)] + str(percentage)

    def calculate_result(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except Exception:
            self.expression = ""

    def get_last_number(self):
        last_number = ""
        for char in reversed(self.expression):
            if char.isdigit() or char == ".":
                last_number = char + last_number
            else:
                break
        return last_number


app = QApplication([])
dastur = Dastur()
dastur.show()
sys.exit(app.exec_())