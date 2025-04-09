from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from app.models.user import *
from app.utils.validator import validate_user_input

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tambah User")

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.save_button = QPushButton("Simpan")
        self.save_button.clicked.connect(self.save_user)

        self.list_button = QPushButton('List User')
        self.list_button.clicked.connect(self.show_all_users)

        layout = QVBoxLayout()
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.list_button)

        self.setLayout(layout)

    def save_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        errors = validate_user_input(username, password)
        print('errornya adalah : ', errors)
        angka = len(errors)
        print('successnya : ', len(errors) > 1)
        print('tipe datanya : ', type(angka))

        if len(errors) > 0:
            # Ada error, tampilkan ke user
            QMessageBox.warning(self, "Validasi", "\n".join(errors))
        else:
            # Validasi lolos, lanjut simpan user
            user = create_user(username, password)  # misalnya create_user dari controller kamu
            print('usernya : ',user)
            # print('succes : ',user['success'])
            # print('succes : ',user['message'])
            if len(user) < 1:
                QMessageBox.information(self, "Sukses", f"User '{user['username']}' berhasil disimpan!")
                self.username_input.clear()
                self.password_input.clear()
            else:
                QMessageBox.critical(self, "Error", f"Gagal menyimpan user.\n{user['message']}")
    
    def show_all_users(self):
        users = show_all_users()
        list_user = []

        for user in users:
            print({
                "id": user.id,
                "username": user.username,
                "password": user.password
            })
            list_user.append(user)

        print('iuib: ' ,list_user[0].id)
        
