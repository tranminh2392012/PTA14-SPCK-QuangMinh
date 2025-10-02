from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic
import sys

user_infor = ["admin:admin:admin"]
user_infor_list = []
name_user = ""
email_user = ""
password_user = ""
isSignIn = False

class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui",self)
        
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui",self)
   
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
        
        global name_user,email_user,password_user, isSignIn
        name_user = username
        email_user = email
        password_user = password
        isSignIn = True
        
        QMessageBox.information(self, "Thông báo", "Đăng kí thành công")
        login.close()
        lobby.update_username()  # ← Cập nhật username sau khi đăng ký
        lobby.show()                 
        
    def CheckLogin(self):
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        
        if not email or not password:
            QMessageBox.warning(self, "Error", "Vui lòng nhập đầy đủ thông tin")
            return
            
        found = False
        for user in user_infor:
            if email == user.split(":")[1] and password == user.split(":")[2]:
                login.close()
                global name_user,email_user,password_user, isSignIn
                isSignIn = True
                name_user = user.split(":")[0]
                email_user = user.split(":")[1]
                password_user = user.split(":")[2]
                lobby.update_username()
                lobby.show()
                found = True
                break
        
        if not found:
            msg_box.setText("Email hoặc password sai!")
            msg_box.exec()         
                
class Lobby(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("food_app.ui",self)
        
        self.pushButton_6.clicked.connect(self.LogOut)
        self.pushButton_2.clicked.connect(self.Order)
               
        ##nút công cụ chuyển trang        
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0)) 
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1)) 
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))   
        
        ##nút chuyển trang đọc thông tin về các nhà hàng         
        self.pushButton_34.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2)) 
        self.pushButton_56.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4)) 
        self.pushButton_54.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))      
        
        ##nút trở về trang nhà hàng
        self.pushButton_23.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))            
        self.pushButton_28.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1)) 
        self.pushButton_37.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))         
        
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
        self.pushButton_33.clicked.connect(self.tang_so_luong_chicken_nugget)
        self.pushButton_33.clicked.connect(self.total_money)
        
        ##order burger
    def tang_so_luong_burger(self):
        so_luong_burger = int(self.label_95.text())
        so_luong_burger += 1
        self.label_95.setText(str(so_luong_burger))
        self.label_101.setText(str(so_luong_burger))
        print(f"Số lượng burger: {so_luong_burger}")
        
        ##order Hotdog
    def tang_so_luong_hotdog(self):
        so_luong_hotdog = int(self.label_96.text())
        so_luong_hotdog += 1
        self.label_96.setText(str(so_luong_hotdog))
        self.label_102.setText(str(so_luong_hotdog))
        print(f"Số lượng hotdog: {so_luong_hotdog}")

        ##order French fries
    def tang_so_luong_french_fries(self):
        so_luong_french_fries = int(self.label_97.text())
        so_luong_french_fries += 1
        self.label_97.setText(str(so_luong_french_fries))
        self.label_104.setText(str(so_luong_french_fries))
        print(f"Số lượng french fries: {so_luong_french_fries}")
        
        ##order fried chicken
    def tang_so_luong_fried_chicken(self):
        so_luong_fried_chicken = int(self.label_98.text())
        so_luong_fried_chicken += 1
        self.label_98.setText(str(so_luong_fried_chicken))
        self.label_105.setText(str(so_luong_fried_chicken))
        print(f"Số fried chicken: {so_luong_fried_chicken}")

        ##order cheese stick
    def tang_so_luong_cheese_stick(self):
        so_luong_cheese_stick = int(self.label_99.text())
        so_luong_cheese_stick += 1
        self.label_99.setText(str(so_luong_cheese_stick))
        self.label_106.setText(str(so_luong_cheese_stick))
        print(f"Số lượng cheese stick: {so_luong_cheese_stick}")
        
        ##order chicken nugget
    def tang_so_luong_chicken_nugget(self):
        so_luong_chicken_nugget = int(self.label_100.text())
        so_luong_chicken_nugget += 1
        self.label_100.setText(str(so_luong_chicken_nugget))
        self.label_107.setText(str(so_luong_chicken_nugget))
        print(f"Số chicken nugget: {so_luong_chicken_nugget}")
        
    # Tính tổng tiền       
    def total_money(self):
        tong_so_tien = int(self.label_103.text())
        tong_so_tien += 5
        self.label_103.setText(str(tong_so_tien))
        print(f"Số tiền burger: {tong_so_tien}","$")
           
    def update_username(self):
        self.label_38.setText(name_user)
        self.label_58.setText(name_user)
        self.label_59.setText(email_user)
        self.label_60.setText(password_user)
        
    def LogOut(self):
        global name_user,email_user,password_user, isSignIn
        lobby.close()
        isSignIn = False
        name_user = ""
        email_user = ""
        password_user = ""
        login.show()  
        
    def Order(self):
        burger = int(self.label_95.text())
        hotdog = int(self.label_96.text())
        french_fries = int(self.label_97.text())
        fried_chicken = int(self.label_98.text())
        cheese_stick = int(self.label_99.text())
        chicken_nugget = int(self.label_100.text())
        if burger > 0 or hotdog > 0 or french_fries > 0 or fried_chicken > 0 or cheese_stick > 0 or chicken_nugget > 0:
            #burger
            self.label_95.setText("0")
            #hotdog
            self.label_96.setText("0")
            #french fries
            self.label_97.setText("0")
            #fried chicken
            self.label_98.setText("0")
            #cheese stick
            self.label_99.setText("0")
            #chicken nugget
            self.label_100.setText("0")
            #total money
            self.label_103.setText("0")
            msg_box.setText("Đặt hàng thành công!")
            msg_box.exec()
        elif burger == 0:
            msg_box.setText("Chưa có thứ gì được đặt!")
            msg_box.exec()
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    login = Login()
    lobby = Lobby()
    login.show()
    app.exec()