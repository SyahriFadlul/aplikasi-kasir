from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QFrame, QHBoxLayout, QSizePolicy, QTableWidget, 
    QPushButton, QListWidget, QListWidgetItem, QLineEdit, QTabWidget, QSpacerItem
)
from PySide6.QtGui import QPixmap, Qt, QIcon
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QRect

from tests.mocks.mock_product_model import MockProduct
from app.models.product import Product
from controllers.product_controller import ProductController
from .components.base_table import ModularTableView

class ProductPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(600, 0, 300, 800)
        self.setStyleSheet("background-color: #f0f0f0; border-left: 1px solid #ccc;")
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        self.label_title = QLabel("Detail Produk")
        self.label_desc = QLabel("")
        self.label_desc.setWordWrap(True)

        layout.addWidget(self.label_title)
        layout.addWidget(self.label_desc)
        self.setLayout(layout)

    def update_product(self, name, description):
        self.label_title.setText(name)
        self.label_desc.setText(description)

# class TableItems(QWidget):
#     def __init__(self,):

class InventoryManagement(QWidget):
    def __init__(self, stacked_widget):

        super().__init__()
        self.stacked_widget = stacked_widget
        self.title = QLabel('Manajemen Inventaris')
        self.title.setObjectName('title')
        
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #ccc;")

        self.tabs = QTabWidget()
        self.tabs.setObjectName('tabs')
        self.tabs.setTabsClosable(True)

        self.category = QPushButton('kategori')
        self.sort = QPushButton('urutan')
        self.add_btn = QPushButton('tambah produk')
        self.add_btn.clicked.connect(self.to_add_product_page)

        self.search = QLineEdit()
        self.search.setPlaceholderText('pencarian')

        header_layout = QHBoxLayout()
        header_layout.addWidget(self.title)

        layout2 = QHBoxLayout()
        layout2.setContentsMargins(0,20,0,0)
        # layout2.addWidget(self.search)
        # layout2.addWidget(self.category)
        # layout2.addWidget(self.sort)
        layout2.addStretch()
        layout2.addWidget(self.add_btn)

        columns = [
            {"field": "id", "title": "ID"},
            {"field": "name", "title": "Nama Produk"},
            {"field": "unit", "title": "Satuan"},
            {"field": "price", "title": "Harga"},
            {"field": "stock", "title": "Stok"},
        ]


        mock = MockProduct()
        rdata = Product()
        controller = ProductController(rdata)  # List[dict]
        data = controller.get_all_products()
        if data:
            columns = [
                {"field": key, "title": key.replace('_', ' ').title()}
                for key in data[0].keys()
            ]
        else:
            columns = []

        self.table_widget = ModularTableView(columns, data)


        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addLayout(header_layout)
        layout.addWidget(separator)
        layout.addLayout(layout2)
        layout.addWidget(self.table_widget)
        self.setLayout(layout)

    def to_add_product_page(self):
        self.stacked_widget.setCurrentIndex(2)
        print('test')
            
    #     self.product_list = QListWidget(self)
    #     self.product_list.setGeometry(20, 20, 250, 360)
    #     self.product_list.addItem(QListWidgetItem("Produk A"))
    #     self.product_list.addItem(QListWidgetItem("Produk B"))
    #     self.product_list.addItem(QListWidgetItem("Produk C"))
    #     self.product_list.itemClicked.connect(self.show_product_detail)

    #     # Detail Panel (Off-canvas)
    #     self.detail_panel = ProductPanel(self)
    #     self.detail_panel.hide()
    #     self.panel_open = False

    # def show_product_detail(self, item):
    #     name = item.text()
    #     desc = f"Ini deskripsi detail dari {name}. Bisa panjang lebar disini."
    #     self.detail_panel.update_product(name, desc)

    #     if not self.panel_open:
    #         self.toggle_panel(show=True)


    # def toggle_panel(self, show=True):
    #     anim = QPropertyAnimation(self.detail_panel, b"geometry")
    #     anim.setDuration(300)
    #     anim.setEasingCurve(QEasingCurve.OutCubic)

    #     if show and not self.panel_open:
    #         self.detail_panel.show()
    #         anim.setStartValue(QRect(900, 0, 300, 400))
    #         anim.setEndValue(QRect(600, 0, 300, 400))
    #         self.panel_open = True
    #     elif not show and self.panel_open:
    #         anim.setStartValue(QRect(600, 0, 300, 400))
    #         anim.setEndValue(QRect(900, 0, 300, 400))
    #         self.panel_open = False

    #     anim.finished.connect(lambda: self.detail_panel.hide() if not self.panel_open else None)
    #     anim.start()
    #     self.anim = anim  # supaya nggak ke-GC

