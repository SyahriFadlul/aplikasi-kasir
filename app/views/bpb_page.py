from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class BPB_Page(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("Ini Halaman Purchase Order"))
        