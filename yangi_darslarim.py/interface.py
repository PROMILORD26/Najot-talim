from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from os import *
system("cls")

def chiqar():
    print("Javobi:")


def dasturchi():
    app = QApplication([])
    forma = QWidget()
    forma. setWindowTitle("KALKULATOR")
    forma.resize(600, 400)
    forma.move(400, 200)
    label = QLabel(forma)
    label.setGeometry(175, 175, 50, 50)
    forma.setFont(QFont("Calibri", 20))
    label.setText("a ni kiriting:")

    txt = QLineEdit(forma)
    txt.setGeometry(175, 175, 50, 50)
    btn = QPushButton("a son:", forma)

    txt = QLineEdit(forma)
    txt.setGeometry(175, 175, 125, 50)
    btn = QPushButton("b son:", forma)

    btn.setGeometry(175, 175, 125, 50)
    btn.clicked.connect(lambda: chiqar(txt.text()))
    btn.setStyleSheet(""" color: rgb(255, 0, 0);
                      backround-color: yellow;
                      border: 1px solid;
                      border-radius:10px;
                      border-color: green;

    """)
    forma.show()
    sys.exit(app.exec_())

dasturchi()