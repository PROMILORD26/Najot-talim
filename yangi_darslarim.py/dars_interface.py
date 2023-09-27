from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
os.system("cls")

# class Main(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.resize(180, 130)
#         main_login = QPushButton("Login", self)
#         main_register = QPushButton("Register", self)
#         main_login.setGeometry(10, 10, 160, 40)
#         main_register.setGeometry(10, 70, 160, 40)
#         main_login.clicked.connect(self.login)
#         main_register.clicked.connect(self.register)

#     def login(self):
#         self.class_login = Login()
#         self.close()
#         self.class_login.show()

#     def register(self):
#         self.class_register = Register()
#         self.close()
#         self.class_register.show()

    

    

# class Login(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setFont(QFont("Calibri", 16))
#         self.resize(400, 250)
#         self.setWindowTitle("Login")
#         login_lb = QLabel("Login:", self)
#         login_lb.setGeometry(30, 10, 100, 50)
#         login_ln = QLineEdit(self)
#         login_ln.setGeometry(150, 20, 230, 30)
#         login_ln.setPlaceholderText("Enter login...")

#         password_lb = QLabel("Password:", self)
#         password_lb.setGeometry(30, 70, 150, 50)
#         password_ln = QLineEdit(self)
#         password_ln.setGeometry(150, 78, 230, 30)
#         password_ln.setPlaceholderText("Enter password...")

#         login_btn = QPushButton("Log In", self)
#         login_btn.setGeometry(30, 150, 345, 50)
#         login_btn.setStyleSheet("""background-color: rgb(8, 102, 255);
#                                 border-radius: 5px;
#                                 border: 2px solid black;
#                                 """)
        
        
        
# class Register(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.resize(400, 230)
#         self.setFont(QFont("Calibri", 10))
#         self.setWindowTitle("Register")
#         label1 = QLabel(self)
#         label1.setText("Login:")
#         label1.setGeometry(30, 10, 125, 30)
#         label2 = QLabel(self)
#         label2.setText("Password:")
#         label2.setGeometry(30, 50, 125, 30)

#         label3 = QLabel(self)
#         label3.setText("Repeat password:")
#         label3.setGeometry(30, 90, 125, 30)


#         lineedit1 = QLineEdit(self)
#         lineedit1.setGeometry(160, 8, 210, 30)
#         lineedit1.setPlaceholderText("Enter login...")

#         lineedit2 = QLineEdit(self)
#         lineedit2.setGeometry(160, 48, 210, 30)
#         lineedit2.setPlaceholderText("Enter password...")

#         lineedit3 = QLineEdit(self)
#         lineedit3.setGeometry(160, 88, 210, 30)
#         lineedit3.setPlaceholderText("Repeat password...")

#         btn = QPushButton("Submit", self)
#         btn.setGeometry(30, 145, 340, 50)
#         btn.setStyleSheet("""background-color: rgb(8, 102, 255);
#                                 border-radius: 5px;
#                                 border: 2px solid black;
#                  """)
        


# app = QApplication(sys.argv)
# asosiy = Main()
# asosiy.show()
# sys.exit(app.exec_())






################################################################################################################

