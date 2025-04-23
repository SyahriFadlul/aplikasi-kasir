from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QListWidget, QListWidgetItem,
    QHeaderView, QLineEdit, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QComboBox
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
import os

class ModularTableView(QWidget):
    def __init__(self, columns_config, data, parent=None):
        super().__init__(parent)

        self.base_dir = os.path.dirname(__file__)
        self.assets_dir = os.path.join(self.base_dir, '..', '..', 'assets')

        self.columns_config = columns_config  # List of dicts with 'field', 'title', 'sortable', etc
        self.raw_data = data  # List of dicts from controller/model
        self.filtered_data = data.copy()

        self.search_bar = QLineEdit()
        self.search_bar.setMaximumWidth(200)
        self.search_bar.setPlaceholderText("Cari...")
        self.search_bar.textChanged.connect(self.filter_data)

        self.category = QComboBox()
        self.category.setMaximumWidth(130)
        self.category.addItems(['Pilih Kategori', '2', '3'])

        self.filter_btn = QPushButton()
        self.filter_btn.setIcon(QIcon(os.path.join(self.assets_dir, 'filter.png')))
        self.filter_btn.setIconSize(QSize(15, 15))
        self.filter_btn.setMaximumWidth(30)
        self.filter_btn.setMinimumWidth(30)
        self.filter_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        self.filter_btn.setToolTip("Filter")


        self.sort_btn = QPushButton()
        self.sort_btn.setIcon(QIcon(os.path.join(self.assets_dir, 'sort.png')))
        self.sort_btn.setIconSize(QSize(15, 15))
        self.sort_btn.setMaximumWidth(30)
        self.sort_btn.setMinimumWidth(30)
        self.sort_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        self.sort_btn.setToolTip("Urutkan")
        
        self.table = QTableWidget()
        # self.table.setColumnCount(len(columns_config))
        # self.table.setHorizontalHeaderLabels([col['title'] for col in columns_config])
        self.table.setColumnCount(len(columns_config))  # Tambah 1 kolom
        self.table.setHorizontalHeaderLabels([col['title'] for col in columns_config])
    
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSortingEnabled(True)


        self.pagination_layout = QHBoxLayout()
        self.btn_prev = QPushButton("<")
        self.btn_next = QPushButton(">")
        self.page_label = QLabel("Page 1")
        self.current_page = 1
        self.rows_per_page = 10

        self.btn_prev.clicked.connect(self.prev_page)
        self.btn_next.clicked.connect(self.next_page)

        self.pagination_layout.addWidget(self.btn_prev)
        self.pagination_layout.addWidget(self.page_label)
        self.pagination_layout.addWidget(self.btn_next)

        #layout utama
        self.layout = QVBoxLayout()

        #layout header
        self.layout_header = QHBoxLayout()
        self.layout_header.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.layout_header.addWidget(self.search_bar)
        self.layout_header.addWidget(self.category)
        self.layout_header.addStretch()
        self.layout_header.addWidget(self.filter_btn)
        self.layout_header.addWidget(self.sort_btn)

        self.layout.addLayout(self.layout_header)
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.pagination_layout)
        self.setLayout(self.layout)

        self.refresh_table()

    def refresh_table(self):
        start = (self.current_page - 1) * self.rows_per_page
        end = start + self.rows_per_page
        data_slice = self.filtered_data[start:end]

        self.table.setRowCount(len(data_slice))
        
        for row_idx, row_data in enumerate(data_slice):
            for col_idx, config in enumerate(self.columns_config):
                value = str(row_data.get(config['field'], ''))
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(value))

        total_pages = max(1, -(-len(self.filtered_data) // self.rows_per_page))
        self.page_label.setText(f"Page {self.current_page} of {total_pages}")

    def filter_data(self, text):
        keyword = text.lower()
        self.filtered_data = [row for row in self.raw_data if keyword in str(row).lower()]
        self.current_page = 1
        self.refresh_table()

    def next_page(self):
        if self.current_page * self.rows_per_page < len(self.filtered_data):
            self.current_page += 1
            self.refresh_table()

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.refresh_table()
