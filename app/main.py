import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide6.QtWidgets import QApplication

from dotenv import load_dotenv

from views.main_window import MainWindow
from views.login import Login

base_dir = os.path.dirname(__file__)
assets_dir = os.path.join(base_dir, 'assets')

load_dotenv()

app = QApplication(sys.argv)

window = MainWindow(app)

style_path = os.path.join(assets_dir, 'style.qss')
with open(style_path) as f:
        window.setStyleSheet(f.read())
window.show()
sys.exit(app.exec())
# app.exec()