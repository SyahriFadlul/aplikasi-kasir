import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QHBoxLayout, QVBoxLayout, QStackedWidget, QListWidget, QListWidgetItem, QLabel, QPushButton, QAbstractItemView, QSizePolicy
from PySide6.QtCore import QPropertyAnimation, QSize, QSettings
from PySide6.QtGui import QPixmap, Qt, QIcon

from views.dashboard import Dashboard
from views.po_page import PO_Page

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.base_dir = os.path.dirname(__file__)
        self.assets_dir = os.path.join(self.base_dir, '..', 'assets')
        self.app = app
        # self.setGeometry(100,100,25,500)
        self.setWindowTitle('Aplikasi Kasir')

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # layout utama
        layout = QHBoxLayout(main_widget)
        layout.setContentsMargins(0,0,0,0)
        main_widget.setLayout(layout)

        # frame kiri
        self.left_frame = QWidget()
        self.left_frame.setMinimumWidth(50)
        self.left_frame.setMaximumWidth(200)
        self.left_frame.setMinimumHeight(200)
        self.left_frame.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        # menu burger
        self.menu_btn = QPushButton()
        self.menu_btn.setObjectName('menu_btn')

        menu_btn_img_path = os.path.join(self.assets_dir, 'menu.png')
        self.menu_btn.setIcon(QIcon(menu_btn_img_path))
        self.menu_btn.setIconSize(QSize(30, 30)) 

        self.menu_btn.clicked.connect(self.toggle_sidebar)        

        # layout menu burger
        menu_btn_layout = QHBoxLayout()
        menu_btn_layout.addStretch()
        menu_btn_layout.addWidget(self.menu_btn)

        # separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine) 
        separator.setFrameShadow(QFrame.Sunken)
        
        # sidebar       
        self.sidebar = QListWidget(main_widget)
        self.sidebar.setObjectName('sidebar')
        self.sidebar.setMaximumWidth(200)
        self.sidebar.setContentsMargins(10,10,10,10)
        # scrollbar off
        self.sidebar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sidebar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        #animasi sidebar
        self.animation = QPropertyAnimation(self.left_frame, b"size")
        self.animation.setDuration(200)  
        self.sidebar_expanded = True
       
        # sidebar items
        self.menu_list = [
            {
                "name": "Dashboard",
                "icon": os.path.join(self.assets_dir, 'dashboard.png')
            },
            {
                "name": "Purchase Order",
                "icon": os.path.join(self.assets_dir, 'product.png')
            },
            {
                "name": "Purchase Order",
                "icon": os.path.join(self.assets_dir, 'product.png')
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
        left_layout.addLayout(menu_btn_layout)
        left_layout.addWidget(separator)
        left_layout.addWidget(self.sidebar)

        self.left_frame.setLayout(left_layout)

        # frame kanan
        self.right_frame = QStackedWidget()
        self.right_frame.setObjectName('right_frame')
        self.right_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.right_frame.setMinimumWidth(400)
        
        # halaman-halaman
        self.right_frame.addWidget(Dashboard())
        self.right_frame.addWidget(PO_Page())

        self.sidebar.itemClicked.connect(self.change_page)

        # memasukan frame-frame ke layout utama
        layout.addWidget(self.left_frame)
        layout.addWidget(self.right_frame)

        self.init_list_sidebar()

    def init_list_sidebar(self):
        self.sidebar.clear()
        
        for menu in self.menu_list:
            item_new = QListWidgetItem(QIcon(menu.get("icon")), menu.get("name"))
            item_new.setSizeHint(QSize(40, 40))  # Ukuran default saat besar
            self.sidebar.addItem(item_new)

        self.sidebar.setCurrentRow(0)

    def toggle_sidebar(self):
        target_width = 50 if self.sidebar_expanded else 200

        # Set animasi perubahan ukuran sidebar
        self.animation.setEndValue(QSize(target_width, self.left_frame.height()))
        
        # Hide/Show teks pada QListWidgetItem
        for i in range(self.sidebar.count()):
            item = self.sidebar.item(i)
            if self.sidebar_expanded:
                item.setText('')  # Hilangkan teks saat collapse
                item.setSizeHint(QSize(50, 40))  
            else:
                item.setText(self.menu_list[i]["name"])  # Tampilkan kembali teks saat expand
                item.setSizeHint(QSize(200, 40))

        self.sidebar_expanded = not self.sidebar_expanded

        # revert size
        self.animation.finished.connect(lambda: self.left_frame.setMaximumWidth(target_width))

        self.animation.start()
    
    def change_page(self, item):
        index = self.sidebar.row(item)

        self.right_frame.setCurrentIndex(index)