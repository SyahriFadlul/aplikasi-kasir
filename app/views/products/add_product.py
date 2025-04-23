from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QSizePolicy, QScrollArea, QLineEdit, QHBoxLayout,
    QComboBox, QFrame, QSpacerItem
)
from PySide6.QtGui import QIcon, Qt, QCursor
from PySide6.QtCore import QSize
import os

class CustomLineEdit(QLineEdit):
    def __init__(self, placeholder=""):
        super().__init__()
        self.setPlaceholderText(placeholder)
        self.setStyleSheet(self._normal_style())

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.setStyleSheet(self._focus_style())

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.setStyleSheet(self._normal_style())

    def _focus_style(self):
        return """
        QLineEdit {
            border: 2px solid #0078d7;
            border-radius: 6px;
            padding: 3px;
            background: white;
        }
        """

    def _normal_style(self):
        return """
        QLineEdit {
            border: 1px solid #cccccc;
            border-radius: 6px;
            padding: 3px;
            background: #f9f9f9;
        }
        """


class FormField(QWidget):
    def __init__(self, field_type, label_text, placeholder_text=None, items=None ): # field_type:input,combo
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 5, 10, 0)

        self.label = QLabel(label_text)

        if field_type == 'input':
            self.input = CustomLineEdit(placeholder_text)
        elif field_type == 'combo':
            self.input = QComboBox()
            self.input.addItem(placeholder_text)
            self.input.setCurrentIndex(0)  # Default tampil di awal
            self.input.model().item(0).setEnabled(False)  # Disable item pertama
            self.input.addItems(items)
            self.input.setPlaceholderText(placeholder_text)

        layout.addWidget(self.label)
        layout.addWidget(self.input)
        self.setLayout(layout)

class AddProduct(QWidget):
    def __init__(self, stacked_widget, parent=None):
        super().__init__(parent)

        self.base_dir = os.path.dirname(__file__)
        self.assets_dir = os.path.join(self.base_dir, '..','..', 'assets')

        self.stacked_widget = stacked_widget

        # Tombol Kembali
        self.back_btn = QPushButton()
        self.back_btn.setObjectName('back_btn_product')
        self.back_btn.setIcon(QIcon(os.path.join(self.assets_dir, 'back2.png')))
        self.back_btn.setIconSize(QSize(20, 20))
        self.back_btn.setFlat(True)
        self.back_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.back_btn.clicked.connect(self.back_to_main)

        self.title = QLabel('Tambah Barang')
        self.title.setObjectName('title')

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_btn)
        top_layout.addSpacing(5)
        top_layout.addWidget(self.title)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #ccc;")

        self.barcode_number = FormField('input', 'Barcode', 'Scan barcode atau masukkan nomor barcode')
        self.name = FormField('input', 'Nama Barang', 'Nama barang')
        self.category_combo = FormField('combo', 'Kategori', '-- Pilih Kategori --', items=['1','2','3'])
        self.price = FormField('input', 'Harga', 'Rp. 0')
        self.unit = FormField('combo', 'Satuan', '-- Pilih Satuan --', items=['Pcs', 'Kg', 'Ltr'])
        self.qty = FormField('input', 'Jumlah', 'Masukan jumlah barang')
        self.buffer_number = FormField('input', 'Buffer Stok', 'Masukan buffer stok(angka minimal stok)')

        self.cancel_btn = QPushButton('Batalkan')

        self.scan_multiple_btn = QPushButton('Scan Multiple')
        self.scan_multiple_btn.setStyleSheet("background-color: blue; color: white;")

        self.save_btn = QPushButton('Simpan')
        self.save_btn.setStyleSheet("background-color: #4CAF50; color: white;")

        bot_layout = QHBoxLayout()
        bot_layout.setContentsMargins(10, 10, 10, 2)
        bot_layout.addWidget(self.cancel_btn)
        bot_layout.addStretch()
        bot_layout.addWidget(self.scan_multiple_btn)
        bot_layout.addStretch()
        bot_layout.addWidget(self.save_btn)

        # Layout utama
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(self.back_btn)
        # layout.addWidget(self.title)
        layout.addLayout(top_layout)
        layout.addWidget(separator)
        layout.addWidget(self.barcode_number)
        layout.addWidget(self.name)
        layout.addWidget(self.category_combo)
        layout.addWidget(self.price)
        layout.addWidget(self.unit)
        layout.addWidget(self.qty)
        layout.addWidget(self.buffer_number)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addLayout(bot_layout)
        self.setLayout(layout)
        self.setObjectName('add_product')

    def back_to_main(self):
        self.stacked_widget.setCurrentIndex(1) # main inv
