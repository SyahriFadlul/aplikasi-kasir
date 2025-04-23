import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QStackedWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QAbstractItemView, QSizePolicy
from PySide6.QtCore import QPropertyAnimation, QSize, QSettings, QTimer, Signal
from PySide6.QtGui import QPixmap, Qt, QIcon, QCursor

from views.dashboard import Dashboard
from views.po_page import PO_Page
from views.inventory_management import InventoryManagement
from views.products.add_product import AddProduct

class ClickableWidget(QWidget):
    clicked = Signal()

    def __init__(self, icon_path, title, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setObjectName('item_sidebar')

        # Layout utama
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(10)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # Ikon
        self.icon_label = QLabel()
        self.icon_label.setPixmap(QPixmap(icon_path).scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

        # Teks
        self.title_label = QLabel(title)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Tambahkan ke layout
        layout.addWidget(self.icon_label)
        layout.addWidget(self.title_label)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.base_dir = os.path.dirname(__file__)
        self.assets_dir = os.path.join(self.base_dir, '..', 'assets')
        self.app = app
        # self.setGeometry(100,100,25,500)        
        self.setWindowTitle('Aplikasi Kasir')

        main_widget = QWidget()
        main_widget.setObjectName('main')
        self.setCentralWidget(main_widget)

        # layout utama
        layout = QHBoxLayout(main_widget)
        layout.setSpacing(0)
        layout.setContentsMargins(0,0,0,0)
        main_widget.setLayout(layout)

        # logo
        self.logo = QLabel()
        logo_path = os.path.join(self.assets_dir, 'badge.png')
        self.logo.setPixmap(QPixmap(logo_path).scaled(25,25))
        self.title = QLabel('Kasir')
        # self.title.setFrameStyle(QFrame.StyledPanel)

        self.title_main_menu = QLabel('Menu Utama')
        self.title_main_menu.setObjectName('title_main_menu')

        # menu burger
        self.menu_btn = QPushButton()
        self.menu_btn.setObjectName('menu_btn')
        self.menu_btn.setFlat(True)
        self.menu_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.menu_btn_img_path = os.path.join(self.assets_dir, 'arrow-left.png')
        self.menu_btn.setIcon(QIcon(self.menu_btn_img_path))
        self.menu_btn.setIconSize(QSize(20, 20)) 

        self.menu_btn.clicked.connect(self.toggle_sidebar)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center button
        button_layout.addWidget(self.menu_btn)

        # frame top sidebar
        self.top_sidebar_widget = QWidget()
        self.top_sidebar_widget.setObjectName('top_sidebar_widget')
        self.top_sidebar_widget.setMinimumHeight(40)

        # self.top_sidebar_widget.setMinimumWidth(10)
        self.top_sidebar_widget.setMaximumHeight(40)
        # self.top_sidebar_widget.setContentsMargins(0,0,0,0)

        self.top_sidebar_widget.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        # layout top sidebar
        top_sidebar_layout = QHBoxLayout()
        top_sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        top_sidebar_layout.addWidget(self.logo)
        top_sidebar_layout.addWidget(self.title)
        top_sidebar_layout.addStretch()
        top_sidebar_layout.addLayout(button_layout)
        self.top_sidebar_widget.setLayout(top_sidebar_layout)

        # separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine) 
        separator.setFrameShadow(QFrame.Sunken)
        
        # sidebar       
        self.sidebar = QListWidget(main_widget)
        self.sidebar.setObjectName('sidebar')
        self.sidebar.setMaximumWidth(600)
        self.sidebar.setContentsMargins(10,10,10,10)
        self.sidebar.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        # scrollbar off
        self.sidebar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sidebar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # new sidebar version
        self.rsidebar = QWidget()
        self.rsidebar.setObjectName('rsidebar')
        self.rsidebar.setMinimumWidth(200)
        self.rsidebar.setMaximumWidth(200)

        # sidebar items
        self.menu_list = [
            {
                "name": "Ringkasan",
                "icon": os.path.join(self.assets_dir, 'overview.png')
            },
            {
                "name": "Inventaris",
                "icon": os.path.join(self.assets_dir, 'box.png')
            },
            {
                "name": "Penjualan",
                "icon": os.path.join(self.assets_dir, 'cart4.png')
            },
            {
                "name": "Setting",
                "icon": os.path.join(self.assets_dir, 'setting.png')
            },

        ]

        self.Overview = ClickableWidget(self.menu_list[0]['icon'], self.menu_list[0]['name']) #dashboard
        self.Overview.setObjectName('sidebar_items')
        self.Overview.clicked.connect(lambda: self.change_page(self.Overview))
        self.Inventory = ClickableWidget(self.menu_list[1]['icon'], self.menu_list[1]['name'])
        self.Inventory.setObjectName('sidebar_items')
        self.Inventory.clicked.connect(lambda: self.change_page(self.Inventory))
        self.Sales = ClickableWidget(self.menu_list[2]['icon'], self.menu_list[2]['name'])
        self.Sales.setObjectName('sidebar_items')
        self.Sales.clicked.connect(lambda: self.change_page(self.Sales))
        self.Setting = ClickableWidget(self.menu_list[3]['icon'], self.menu_list[3]['name'])
        self.Setting.setObjectName('sidebar_items')
        self.Setting.clicked.connect(lambda: self.change_page(self.Setting))

        self.test = QPushButton()
        self.test_path = os.path.join(self.assets_dir, 'arrow-left.png')
        self.test.setIcon(QIcon(self.test_path))
        self.test.setIconSize(QSize(20, 20))
        self.test.setText('test')
        self.test.setObjectName('tests')

        layout_btn = QHBoxLayout()
        layout_btn.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout_btn.addWidget(self.test)
            
        self.rsidebar_layout = QVBoxLayout()
        self.rsidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.rsidebar_layout.addWidget(self.top_sidebar_widget)
        self.rsidebar_layout.addWidget(self.Overview)
        self.rsidebar_layout.addWidget(self.Inventory)
        self.rsidebar_layout.addWidget(self.Sales)
        self.rsidebar_layout.addWidget(self.Setting)
        self.rsidebar_layout.addWidget(self.test)
        self.rsidebar.setLayout(self.rsidebar_layout)
        #animasi sidebar
        # # self.animation = QPropertyAnimation(self.left_frame, b"size")
        # self.animation.setDuration(200)  
        self.sidebar_expanded = True
       

        # bagian kanan
        self.right_section = QStackedWidget()
        self.right_section.setObjectName('right_section')
        self.right_section.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.right_section.setMinimumWidth(400)
        
        # halaman-halaman
        self.right_section.addWidget(Dashboard())
        self.right_section.addWidget(InventoryManagement(self.right_section))
        self.right_section.addWidget(AddProduct(self.right_section))
        self.right_section.addWidget(PO_Page())

        self.sidebar.itemClicked.connect(self.change_page)

        # memasukan frame-frame ke layout utama
        # layout.addWidget(self.left_section)
        layout.addWidget(self.rsidebar)
        layout.addWidget(self.right_section)

        # self.init_list_sidebar()

    def init_sidebar_items(self, icon_path, title):
        self.item_sidebar = QWidget()
        # self.item_sidebar.setObjectName('item_sidebar')
        self.item_sidebar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        self.label_icon = QLabel()
        self.label_icon.setPixmap(QPixmap(icon_path).scaled(20, 20))
        self.label_icon.setObjectName('label_icon')

        self.label_title = QLabel(title)
        self.label_title.setObjectName('label_title')
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeft)

        item_sidebar_layout = QHBoxLayout()
        item_sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        item_sidebar_layout.addWidget(self.label_icon)
        item_sidebar_layout.addSpacing(0)
        item_sidebar_layout.addWidget(self.label_title)
        self.item_sidebar.setLayout(item_sidebar_layout)
        self.item_sidebar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor)) 

        return self.item_sidebar
        # self.rsidebar_layout.addWidget(self.item_sidebar)


    def init_list_sidebar(self):
        self.sidebar.clear()

        self.sidebar.setIconSize(QSize(20, 20))
        self.sidebar.itemAlignment()
        
        for menu in self.menu_list:
            item_new = QListWidgetItem(QIcon(menu.get("icon")), menu.get("name"))
            item_new.setSizeHint(QSize(40, 40))  # Ukuran default saat besar
            self.sidebar.addItem(item_new)

        self.sidebar.setCurrentRow(0)

    def init_list_rsidebar(self):
        self.rsidebar.clear()

        # self.sidebar.setIconSize(QSize(20, 20))
        # self.sidebar.itemAlignment()
        
        for menu in self.menu_list:
            item_new = QListWidgetItem(QIcon(menu.get("icon")), menu.get("name"))
            item_new.setSizeHint(QSize(40, 40))  # Ukuran default saat besar
            self.sidebar.addItem(item_new)

        self.sidebar.setCurrentRow(0)

    def toggle_sidebar(self):
        print('toggle sidebar')
        self
        
        self.sidebar_expanded = not self.sidebar_expanded

        if not self.sidebar_expanded: #collapsed
            self.rsidebar.setMinimumWidth(65)
            self.rsidebar.setMaximumWidth(65)
            self.rsidebar.setMinimumHeight(200)

            self.top_sidebar_widget.setMaximumWidth(50)
            self.top_sidebar_widget.setMaximumHeight(50)

            self.logo.setHidden(True)
            self.title.setHidden(True)
            self.title_main_menu.setHidden(True)            

            self.menu_btn_img_path = os.path.join(self.assets_dir, 'arrow-right.png')
            self.menu_btn.setIcon(QIcon(self.menu_btn_img_path))
        else:
            self.rsidebar.setMaximumWidth(250)

            self.top_sidebar_widget.setMaximumWidth(250)
            self.top_sidebar_widget.setMaximumHeight(50)

            self.logo.setHidden(False)
            self.title.setHidden(False)
            self.title.setText('Kasir')
            self.title_main_menu.setHidden(False)

            # self.left_section.setObjectName('left_section')
            self.menu_btn_img_path = os.path.join(self.assets_dir, 'arrow-left.png')
            self.menu_btn.setIcon(QIcon(self.menu_btn_img_path))
    
    def change_page(self, item):
        print(item.title_label.text())


        # self.right_section.setCurrentIndex(index)

    def handle_sidebar_click(self, index):
        self.right_section.setCurrentIndex(index)
