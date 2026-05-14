import sys

from asset_creation import create_asset
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import(QLabel, QVBoxLayout, QLineEdit, QComboBox, QDoubleSpinBox, QPushButton, QMainWindow, QApplication, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VFX Asset Pipeline")

        layout = QVBoxLayout()

        self.textbox = QLineEdit()
        self.textbox.setMaxLength(10)
        self.textbox.setPlaceholderText("Enter Asset Name")

        layout.addWidget(QLabel("Asset Name"))
        layout.addWidget(self.textbox)

        self.combobox = QComboBox()
        self.combobox.addItems(["Characters", "Props", "Environments"])

        layout.addWidget(QLabel("Asset Type"))
        layout.addWidget(self.combobox)

        self.Btn = QPushButton(text="Create Asset", parent=self)
        self.Btn.setFixedSize(100, 60)
        self.Btn.clicked.connect(self.create_asset)

        layout.addWidget(self.Btn)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def create_asset(self):
        create_asset(self.textbox.text(), self.combobox.currentText())




app = QApplication(sys.argv)

window = MainWindow()
window.setMinimumWidth(400)
window.show()
sys.exit(app.exec())