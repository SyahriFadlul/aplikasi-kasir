import sys, os

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QPropertyAnimation, QSize, QSettings

from ui.home import Ui_Cashier

# class MainApp(QMainWindow, Ui_Cashier):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)  # Panggil setupUi untuk inisialisasi GUI

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainApp()
#     window.show()
#     sys.exit(app.exec())
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Cashier()
        self.ui.setupUi(self)
        # uic.loadUi("test.ui", self)
        
        # ui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test.ui"))
        # self.ui = uic.loadUi(ui_path, self)

        self.ui.toggle_sidebar_button.setText("S")

        # Animasi untuk Sidebar
        self.animation = QPropertyAnimation(self.ui.sidebar, b"size")
        self.animation.setDuration(100)  # Durasi animasi dalam ms
        self.sidebar_expanded = True

        # Hubungkan tombol dengan fungsi toggle
        self.ui.toggle_sidebar_button.clicked.connect(self.toggle_sidebar)

        # Pulihkan posisi dan ukuran jendela
        # self.settings = QSettings("MyCompany", "MyApp")
        # self.restoreGeometry(self.settings.value("geometry", b""))

    def toggle_sidebar(self):
        if self.sidebar_expanded:
            self.animation.setEndValue(QSize(50, self.ui.sidebar.height()))  # Mengecil
        else:
            self.animation.setEndValue(QSize(200, self.ui.sidebar.height()))  # Membesar
        self.sidebar_expanded = not self.sidebar_expanded
        self.animation.start()


    def closeEvent(self, event):
        #  Simpan posisi dan ukuran jendela sebelum aplikasi ditutup
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

app = QApplication([])
window = MainWindow()
window.show()
sys.exit(app.exec())
# app.exec_()