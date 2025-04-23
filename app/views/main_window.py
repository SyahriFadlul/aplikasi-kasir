import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFrame, QHBoxLayout, QVBoxLayout, 
    QStackedWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QAbstractItemView, QSizePolicy
    )
from PySide6.QtCore import QPropertyAnimation, QSize, QSettings
from PySide6.QtGui import QPixmap, Qt, QIcon

from views.dashboard import Dashboard
from views.po_page import PO_Page
from views.inventory_management import InventoryManagement
from views.products.add_product import AddProduct

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

        # frame kiri
        self.left_section = QFrame()
        self.left_section.setObjectName('left_section')
        self.left_section.setContentsMargins(5,5,5,5)
        self.left_section.setMinimumWidth(200)
        self.left_section.setMaximumWidth(250)
        self.left_section.setMinimumHeight(200)
        self.left_section.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        # frame top sidebar
        self.top_sidebar_frame = QFrame()
        self.top_sidebar_frame.setObjectName('top_sidebar_frame')
        # self.top_sidebar_frame.setMinimumWidth(10)
        self.top_sidebar_frame.setMaximumHeight(42)
        # self.top_sidebar_frame.setContentsMargins(0,0,0,0)
        self.top_sidebar_frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        # logo
        self.logo = QLabel()
        logo_path = os.path.join(self.assets_dir, 'badge.png')
        self.logo.setPixmap(QPixmap(logo_path).scaled(25,25))
        self.title = QLabel('Kasir')

        self.title_main_menu = QLabel('Menu Utama')
        self.title_main_menu.setObjectName('title_main_menu')

        # menu btn
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


        # layout top sidebar
        top_sidebar_layout = QHBoxLayout()
        top_sidebar_layout.addWidget(self.logo)
        top_sidebar_layout.addWidget(self.title)
        top_sidebar_layout.addStretch()
        top_sidebar_layout.addLayout(button_layout)
        self.top_sidebar_frame.setLayout(top_sidebar_layout)
        top_sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        
        #animasi sidebar
        # # self.animation = QPropertyAnimation(self.left_frame, b"size")
        # self.animation.setDuration(200)  
        self.sidebar_expanded = True
       
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

        # layout frame kiri
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(10,10,10,10)
        # items layout frame kiri
        left_layout.addWidget(self.top_sidebar_frame)
        left_layout.addWidget(self.title_main_menu)
        left_layout.addWidget(separator)
        left_layout.addWidget(self.sidebar)

        self.left_section.setLayout(left_layout)

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
        layout.addWidget(self.left_section)
        layout.addWidget(self.right_section)

        self.init_list_sidebar()

    def init_list_sidebar(self):
        self.sidebar.clear()

        self.sidebar.setIconSize(QSize(20, 20))
        self.sidebar.itemAlignment()
        
        for menu in self.menu_list:
            item_new = QListWidgetItem(QIcon(menu.get("icon")), menu.get("name"))
            item_new.setSizeHint(QSize(40, 40))  # Ukuran default saat besar
            self.sidebar.addItem(item_new)

        self.sidebar.setCurrentRow(0)

    def toggle_sidebar(self):
        self.left_section.setContentsMargins(1,1,1,1)
        # clear listwidgetnya, declare ulang, masukin ke if sidebarexpanded
        # Hide/Show teks pada QListWidgetItem
        for i in range(self.sidebar.count()):
            item = self.sidebar.item(i)
            print(item.flags())
            if self.sidebar_expanded:
                item.setText(None)  # Hilangkan teks saat collapse
                item.setSizeHint(QSize(50, 40))  
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  
            else:
                item.setText(self.menu_list[i]["name"])  # Tampilkan kembali teks saat expand
                item.setSizeHint(QSize(200, 40))
                item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter)  
        
        self.sidebar_expanded = not self.sidebar_expanded

        if not self.sidebar_expanded: #collapsed
            self.left_section.setMinimumWidth(65)
            self.left_section.setMaximumWidth(65)
            self.left_section.setMinimumHeight(200)

            self.top_sidebar_frame.setMaximumWidth(50)

            self.logo.setHidden(True)
            self.title.setHidden(True)
            self.title_main_menu.setHidden(True)
            
            self.top_sidebar_frame.setFrameStyle(QFrame.NoFrame)

            self.menu_btn_img_path = os.path.join(self.assets_dir, 'arrow-right.png')
            self.menu_btn.setIcon(QIcon(self.menu_btn_img_path))
        else:
            self.left_section.setMaximumWidth(250)

            self.top_sidebar_frame.setMaximumWidth(250)

            self.logo.setHidden(False)
            self.title.setHidden(False)
            self.title.setText('Kasir')
            self.title_main_menu.setHidden(False)

            # self.left_section.setObjectName('left_section')
            self.menu_btn_img_path = os.path.join(self.assets_dir, 'arrow-left.png')
            self.menu_btn.setIcon(QIcon(self.menu_btn_img_path))
    
    def change_page(self, item):
        index = self.sidebar.row(item)

        self.right_section.setCurrentIndex(index)