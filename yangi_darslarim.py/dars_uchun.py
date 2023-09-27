from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

os.system("cls")
class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1400, 900)
        self.setStyleSheet("""background-color: rgb(8, 102, 255);
                           font-size: 35px;""")
        self.setWindowIcon(QIcon("C:\\Users\\HP\\Downloads\\face.jpeg"))
        self.setWindowTitle("Facebook")
        lbl = QLabel(self)
        lbl.move(500, 300)
        lbl.resize(400, 100)
        lbl.setText("Facebookga hush kelibsiz")
        login = QPushButton("Login", self)
        login.setGeometry(500, 400, 200, 50)
        login.setStyleSheet("""background-color: white;
                            border-radius: 5px;
                            border-weight: 3px;
                            border: 4px solid yellow;
                            """)
        register = QPushButton("register", self)
        register.setGeometry(750, 400, 200, 50)
        register.setStyleSheet("""background-color: white;
                            border-radius: 5px;
                            border-weight: 3px;
                            border: 4px solid yellow;
                            """)
        login.clicked.connect(self.login)
        register.clicked.connect(self.register)
    
    def login(self):
        self.class_login = Login()
        self.close()
        self.class_login.show()

    def register(self):
        self.class_register = Register()
        self.close()
        self.class_register.show()

        

class Register(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1000, 800)
        self.setFont(QFont("Calibri", 16))
        self.setWindowTitle("Register")
        self.setWindowIcon(QIcon("C:\\Users\\HP\\Downloads\\face.jpeg"))
        label1 = QLabel(self)
        label1.setText("Login")
        label1.setGeometry(350, 150, 250, 50)
        label2 = QLabel(self)
        label2.setText("Password")
        label2.setGeometry(350, 250, 250, 50)

        label3 = QLabel(self)
        label3.setText("Repeat password")
        label3.setGeometry(350, 350, 250, 50)


        lineedit1 = QLineEdit(self)
        lineedit1.setGeometry(350, 200, 250, 50)

        lineedit2 = QLineEdit(self)
        lineedit2.setGeometry(350, 300, 250, 50)

        lineedit3 = QLineEdit(self)
        lineedit3.setGeometry(350, 400, 250, 50)
        btn = QPushButton("Submit", self)
        btn.setGeometry(350, 475, 250, 50)

        
    def to_login(self):
        self.oyna1 = Login()
        self.close()
        self.oyna1.show()
        





class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(640, 480)
        self.setWindowTitle("Login")
        self.setStyleSheet("background-color: yellow;")
        





















app = QApplication(sys.argv)
asosiy = Main()
asosiy.show()
sys.exit(app.exec_())












































# QMessageBox metodlari
# 1. seticon()
#       a) Error
#       b) Warning
#       c) Information  
#       d) Question  
# 2. setText()
# 3. settitle()
# 4. setInformative()
# 5. setStandartButton()
#       a) QMessegeBox.Ok
#       b) QMessegeBox.Yes
#       c) QMessegeBox.No
#       d) QMessegeBox.Cancel
#       e) QMessegeBox.Save
#       f) QMessegeBox.Close
#       g) QMessegeBox.Abort
#       h) QMessegeBox.Ignore
#       i) QMessegeBox.Retry