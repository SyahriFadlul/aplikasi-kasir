import sys, os

from PySide6.QtWidgets import QApplication

from views.mainwindow import MainWindow

base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')

app = QApplication(sys.argv)
window = MainWindow(app)

style_path = os.path.join(assets_dir, 'style.qss')
with open(style_path) as f:
        window.setStyleSheet(f.read())
window.show()
sys.exit(app.exec())
# app.exec()