from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Setting(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("Ini Halaman Purchase Order"))
        