from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QHBoxLayout, QSizePolicy, QTableWidget, QGridLayout
from PySide6.QtGui import QPixmap, Qt, QIcon
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

class InfoCard (QFrame):
    def __init__(self, title, value, parent=None):
        super().__init__(parent)
        self.setObjectName('infoCard')
        self.setFrameStyle(QFrame.StyledPanel)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)  # Agar fleksibel saat window berubah

        # Layout untuk card
        layout = QVBoxLayout()
        layout.addWidget(QLabel(title))
        layout.addWidget(QLabel(value))
        self.setLayout(layout)

class InfoTable (QFrame):
    def __init__(self, title, value, parent=None):
        super().__init__(parent)
        self.setObjectName('infoCard')
        self.setFrameStyle(QFrame.StyledPanel)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)  # Agar fleksibel saat window berubah

        # Layout untuk card
        layout = QVBoxLayout()
        layout.addWidget(QLabel(title))
        layout.addWidget(QLabel(value))
        self.setLayout(layout)

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.title = QLabel("Dashboard")
        self.title.setObjectName('title')

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #ccc;")

        income_card = InfoCard('Pemasukan', 'Rp. 10.000')
        expense_card = InfoCard('Pengeluaran', 'Rp. 5.000')
        product_sold_card = InfoCard('Barang Terjual', '700')
        product_count_card = InfoCard('Barang', '1000')

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.plot([0,1,2,3], [5,10,8,15])

        self.graph_frame = QFrame()

        self.warning_table = QFrame()
        self.warning_table.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)

        layout_grid = QGridLayout()

        layout_grid.addWidget(income_card, 0,0,)
        layout_grid.addWidget(expense_card, 0,1)
        layout_grid.addWidget(product_count_card, 0,2)
        layout_grid.addWidget(product_sold_card, 0,3)

        # Layout atas 
        layout1 = QHBoxLayout()
        layout1.addWidget(income_card)
        layout1.addWidget(expense_card)
        layout1.addWidget(product_sold_card)
        layout1.addWidget(product_count_card)
        layout1.setStretch(0, 1)
        layout1.setStretch(1, 1)
        layout1.setStretch(0, 2)
        layout1.setStretch(1, 2)

        # layout kedua
        layout2 = QHBoxLayout()
        layout2.addWidget(self.canvas)

        self.graph_frame.setLayout(layout2)
        
        # Layout utama
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.title)  # Judul
        layout.addWidget(separator)  # Judul
        layout.addLayout(layout_grid)
        layout.addWidget(self.graph_frame)
        self.setLayout(layout)