from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from os import *
system("cls")

class Dastur(QMainWindow):
    def __init__(forma):
        QMainWindow.__init__(forma)
        forma.setWindowTitle("CALCUYATOR")
        forma.resize(360, 670)
        forma.move(1455, 30)
        forma.setStyleSheet("""background-color: black;""")
        forma.exoression = ""

        ac = QPushButton("AC", forma)
        ac.setGeometry(25, 260, 70, 50)
        ac.setFont(QFont("Calibri", 24))
        forma.setStyleSheet("""background-color: ryb(147, 145, 141);
        color: azure;
        border-radius: 35px; """)
        ac.clicked.connect(forma.clear_expression)

        ishora = QPushButton("+/-", forma)
        ishora.setGeometry(105, 260, 70, 50)
        ishora.setStyleSheet("""background-color: rbg(147, 145, 141)color azure;
        border-radius: 35px;      
                               """)
        ishora.clicked.connect(forma.toggle_sign)

        foiz = QPushButton("%", forma)
        foiz.setGeometry(185, 260, 70, 50)
        foiz.setStyleSheet("""background-color: rbg(147, 145, 141)color azure;
        border-radius: 35px;      
                               """)
        ishora.clicked.connect(forma.calculate_percentage)
        
        bolish = QPushButton("/", forma)
        bolish.setGeometry(265, 265, 70, 50)
        bolish.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")
        bolish.clicked.connect(lambda: forma.append_operator("/"))

        yetti = QPushButton("7", forma)
        yetti.setGeometry(25, 340, 70, 70)
        yetti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        yetti.clicked.connect(lambda: forma.append_number("7"))

        sakiz = QPushButton("8", forma)
        sakiz.setGeometry(105, 340, 70, 70)
        sakiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        sakiz.clicked.connect(lambda: forma.append_number("8"))

        toqqiz = QPushButton("9", forma)
        toqqiz.setGeometry(185, 340, 70, 70)
        toqqiz.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        toqqiz.clicked.connect(lambda: forma.append_number("9"))

        kopaytirma = QPushButton("x", forma)
        kopaytirma.setGeometry(265, 340, 70, 70)
        kopaytirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")
        kopaytirma.clicked.connect(lambda: forma.append_operator("*"))

        tort = QPushButton("4", forma)
        tort.setGeometry(25, 415, 70, 70)
        tort.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        tort.clicked.connect(lambda: forma.append_number("4"))

        besh = QPushButton("5", forma)
        besh.setGeometry(105, 415, 70, 70)
        besh.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        besh.clicked.connect(lambda: forma.append_number("5"))

        olti = QPushButton("6", forma)
        olti.setGeometry(185, 415, 70, 70)
        olti.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        olti.clicked.connect(lambda: forma.append_number("6"))
    
        ayirma = QPushButton("-", forma)
        ayirma.setGeometry(265, 415, 70, 70)
        ayirma.setStyleSheet("""background-color : rgb(208, 137, 13);
                        color: azure;
                        border-radius : 35px;""")
        ayirma.clicked.connect(lambda: forma.append_operator("-"))

        bir = QPushButton("1", forma)
        bir.setGeometry(25, 490, 70, 70)
        bir.setStyleSheet("""background-color : rgb(continued)""")

        bir.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        bir.clicked.connect(lambda: forma.append_number("1"))

        ikki = QPushButton("2", forma)
        ikki.setGeometry(105, 490, 70, 70)
        ikki.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        ikki.clicked.connect(lambda: forma.append_number("2"))

        uch = QPushButton("3", forma)
        uch.setGeometry(185, 490, 70, 70)
        uch.setStyleSheet("""background-color : rgb(58, 57, 55);
                        color: azure;
                        border-radius : 35px;""")
        uch.clicked.connect(lambda: forma.append_number("3"))

        qoshish = QPushButton("+", forma)
        qoshish.setGeometry(265, 490, 70, 70)
        qoshish.setStyleSheet("""background-color : rgb(208, 137, 13);
                                color: azure;
                                border-radius : 35px;""")
        qoshish.clicked.connect(lambda: forma.append_operator("+"))

        nol = QPushButton("0          ", forma)
        nol.setGeometry(25, 565, 150, 70)
        nol.setStyleSheet("""background-color : rgb(58, 57, 55);
                                color: azure;
                                border-radius : 35px;""")
        nol.clicked.connect(lambda: forma.append_number("0"))

        nuqta = QPushButton(".", forma)
        nuqta.setGeometry(185, 565, 70, 70)
        nuqta.setStyleSheet("""background-color : rgb(58, 57, 55);
                                color: azure;
                                border-radius : 35px;""")
        nuqta.clicked.connect(lambda: forma.append_decimal())

        teng = QPushButton("=", forma)
        teng.setGeometry(265, 565, 70, 70)
        teng.setStyleSheet("""background-color : rgb(208, 137, 13);
                                color: azure;
                                border-radius : 35px;""")
        teng.clicked.connect(forma.calculate_result)

    def append_number(forma, number):
        forma.expression += number

    def append_operator(forma, operator):
        forma.expression += operator

    def append_decimal(forma):
        if forma.expression and forma.expression[-1].isdigit():
            forma.expression += "."

    def clear_expression(forma):
        forma.expression = ""

    def toggle_sign(forma):
        if forma.expression and forma.expression[-1].isdigit():
            last_number = forma.get_last_number()
            if last_number.startswith("-"):
                forma.expression = forma.expression[:-len(last_number)] + last_number[1:]
            else:
                forma.expression = forma.expression[:-len(last_number)] + "-" + last_number

    def calculate_percentage(forma):
        last_number = forma.get_last_number()
        if last_number and last_number.isdigit():
            percentage = float(last_number) / 100
            forma.expression = forma.expression[:-len(last_number)] + str(percentage)

    def calculate_result(forma):
        try:
            result = eval(forma.expression)
            forma.expression = str(result)
        except Exception:
            forma.expression = ""

    def get_last_number(forma):
        last_number = ""
        for char in reversed(forma.expression):
            if char.isdigit() or char == ".":
                last_number = char + last_number
            else:
                break
        return last_number


app = QApplication([])
dastur = Dastur()
dastur.show()
sys.exit(app.exec_())
