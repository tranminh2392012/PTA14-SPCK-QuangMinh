from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic
import sys

user_infor = ["admin:admin:admin"]
user_infor_list = []
name_user = ""

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui",self)
        
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui",self)
        
        
        #đổi tên username
        
        
        #nút order
    
        
        
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        
        self.pushButton.clicked.connect(self.CheckLogin)
        self.pushButton_5.clicked.connect(self.CheckSignin)
        
    def CheckSignin(self):
        username = self.lineEdit_4.text()
        email = self.lineEdit_3.text()
        password = self.lineEdit_5.text()
        if not email or not password:
            QMessageBox.warning(self, "Error", "Vui lòng nhập đầy đủ thông tin")
            return 
        for user in user_infor:
            if email == user.split(":")[1]:
                QMessageBox.warning(self, "Error", "Email đã được sử dụng")
                return
            
        user_infor.append(f"{username}:{email}:{password}")
        print(user_infor)
        global name_user
        name_user = username
        print(name_user)
        QMessageBox.information(self, "Thông báo", "Đăng kí thành công")
        login.close()
        lobby = Lobby()
        lobby.show()
            # a = user_infor.split(":")
            # a[0] = name
            # a[1] = email
            # a[2] = password
            # user_infor_list.append(name)
            # user_infor_list.append(email)
            # user_infor_list.append(password)
            
            
        
    def CheckLogin(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if email == user_infor_list[0] and password == user_infor_list[1]:
            login.close()
            lobby = Lobby()
            lobby.show()
        else:
            msg_box.setText("Vui long kiem tra thong tin dang nhap")
            msg_box.exec()
            
class Lobby(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("food_app.ui",self)
        self.label_38.setText(name_user)
         
        # self.pushButton_2.click.connect(self.Order)
        
    # def Order(self):
        # if self.label_95.text() != "0":
            
    # def infor(self):
    #     for user in user_infor:
            
        
        ##nút chuyển trang
    
        
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0)) 
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1)) 
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))                 
        
        ##nút chuyển trang
        self.pushButton_27.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))    
        self.pushButton_23.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))        
        
        ##order burger
        self.pushButton_10.clicked.connect(self.tang_so_luong_burger)
        self.pushButton_10.clicked.connect(self.total_money)
        
        ##order Hotdog
        self.pushButton_18.clicked.connect(self.tang_so_luong_hotdog)
        self.pushButton_18.clicked.connect(self.total_money)
        
        ##order cheese stick
        self.pushButton_32.clicked.connect(self.tang_so_luong_cheese_stick)
        self.pushButton_32.clicked.connect(self.total_money)
        
        ##order fried chicken
        self.pushButton_31.clicked.connect(self.tang_so_luong_fried_chicken)
        self.pushButton_31.clicked.connect(self.total_money)
        
        ##order French fries
        self.pushButton_19.clicked.connect(self.tang_so_luong_french_fries)
        self.pushButton_19.clicked.connect(self.total_money)
        
        ##order chicken nugget
        self.pushButton_33.clicked.connect(self.tang_so_luong_hotdog)
        self.pushButton_33.clicked.connect(self.total_money)
        
        ##order onion ring
        self.pushButton_8.clicked.connect(self.tang_so_luong_onion_ring)
        self.pushButton_8.clicked.connect(self.total_money)
        
        ##order tacos 
        self.pushButton_7.clicked.connect(self.tang_so_luong_tacos)
        self.pushButton_7.clicked.connect(self.total_money)
        
        
        ##order burger
    def tang_so_luong_burger(self):
        so_luong_burger = int(self.label_95.text())
        so_luong_burger += 1
        self.label_95.setText(str(so_luong_burger))
        print(f"Số lượng burger: {so_luong_burger}")
        
        ##order Hotdog
    def tang_so_luong_hotdog(self):
        so_luong_hotdog = int(self.label_96.text())
        so_luong_hotdog += 1
        self.label_96.setText(str(so_luong_hotdog))
        print(f"Số lượng hotdog: {so_luong_hotdog}")

        ##order French fries
    def tang_so_luong_french_fries(self):
        so_luong_french_fries = int(self.label_97.text())
        so_luong_french_fries += 1
        self.label_97.setText(str(so_luong_french_fries))
        print(f"Số lượng french fries: {so_luong_french_fries}")
        
        ##order fried chicken
    def tang_so_luong_fried_chicken(self):
        so_luong_fried_chicken = int(self.label_98.text())
        so_luong_fried_chicken += 1
        self.label_98.setText(str(so_luong_fried_chicken))
        print(f"Số fried chicken: {so_luong_fried_chicken}")

        ##order cheese stick
    def tang_so_luong_cheese_stick(self):
        so_luong_cheese_stick = int(self.label_99.text())
        so_luong_cheese_stick += 1
        self.label_99.setText(str(so_luong_cheese_stick))
        print(f"Số lượng cheese stick: {so_luong_cheese_stick}")
        
        ##order chicken nugget
    def tang_so_luong_hotdog(self):
        so_luong_hotdog = int(self.label_100.text())
        so_luong_hotdog += 1
        self.label_100.setText(str(so_luong_hotdog))
        print(f"Số chicken nugget: {so_luong_hotdog}")

        ##order onion ring       
    def tang_so_luong_onion_ring(self):
        so_luong_onion_ring = int(self.label_101.text())
        so_luong_onion_ring += 1
        self.label_101.setText(str(so_luong_onion_ring))
        print(f"Số lượng onion ring: {so_luong_onion_ring}")
        
        ##order tacos       
    def tang_so_luong_tacos(self):
        so_luong_tacos = int(self.label_102.text())
        so_luong_tacos += 1
        self.label_102.setText(str(so_luong_tacos))
        print(f"Số tacos: {so_luong_tacos}")


    # Tính tổng tiền       
    def total_money(self):
        tong_so_tien = int(self.label_103.text())
        tong_so_tien += 5   
        self.label_103.setText(str(tong_so_tien))
        print(f"Số tiền burger: {tong_so_tien}","$")
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    login = Login()
    
    login.show()
    app.exec()