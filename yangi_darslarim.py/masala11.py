from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtBoundSignal
from PyQt5.QtWidgets import *
import sys
from os import system

system("cls")

# class Dastur(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         oyna = QWidget()
#         oyna.setFont(QFont('Calibri', 20))
#         kopaytirish = QLabel(' * ', oyna)
#         kopaytirish.setGeometry(50, 50, 500, 500)
      
#         kopaytirish = QHBoxLayout()
#         oyna.setLayout(kopaytirish)
#         self.setCentralWidget(oyna)

#         oyna.setFont(QFont('Calibri', 20))
#         qoshish = QLabel(' + ', oyna)
#         qoshish.setGeometry(90, 20, 500, 500)
      
#         qoshish = QHBoxLayout()
#         oyna.setLayout(qoshish)
#         self.setCentralWidget(oyna)

#         oyna.setFont(QFont('Calibri', 20))
#         bolish = QLabel(' / ', oyna)
#         bolish.setGeometry(110, 50, 500, 500)
      
#         bolish = QHBoxLayout()
#         oyna.setLayout(bolish)
#         self.setCentralWidget(oyna)

#         oyna.setFont(QFont('Calibri', 20))
#         ayirish = QLabel(' - ', oyna)
#         ayirish.setGeometry(90, 70, 500, 500)
      
#         ayirish = QHBoxLayout()
#         oyna.setLayout(ayirish)
#         self.setCentralWidget(oyna)


# if __name__ == 'main':
#     app = QApplication([])
#     dastur = Dastur()
#     dastur.show()
#     sys.exit(app.exec_())



class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.h_box1 = QHBoxLayout()
        self.btn1 = QLabel("Name: ")
        self.h_box1.addWidget(self.btn1)

        self.ln = QLineEdit()
        self.ln.setPlaceholderText("Enter name...")

        self.h_box1.addWidget(self.ln)

        self.h_box2 = QHBoxLayout()
        self.btn2 = QLabel("Subject: ")
        self.h_box2.addWidget(self.btn2)

        self.ln = QLineEdit()
        self.ln.setPlaceholderText("Enter subject...")
        self.h_box2.addWidget(self.ln)

        self.h_box3=QHBoxLayout()
        self.btn4=QPushButton("+")
        self.h_box3.addWidget(self.btn4)
        self.h_box3.addStretch()
        self.btn8 = QLabel("0")
        self.h_box3.addWidget(self.btn8)
        self.h_box3.addStretch()
        self.btn5=QPushButton("-")
        self.h_box3.addWidget(self.btn5)

        self.h_box4=QHBoxLayout()
        self.btn6=QPushButton("Save")
        self.btn6.setStyleSheet("background-color: green;")
        self.h_box4.addStretch()
        self.h_box4.addWidget(self.btn6)
        self.h_box4.addStretch()
        self.btn7=QPushButton("Exit")
        self.btn7.setStyleSheet("background-color: red;")
        self.h_box4.addStretch()
        self.h_box4.addWidget(self.btn7)
        self.h_box4.addStretch()




        

        
        self.v_box=QVBoxLayout()
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)

        self.setLayout(self.v_box)

       



app = QApplication([])
win = MainWindow()
win.show()
sys.exit(app.exec())

