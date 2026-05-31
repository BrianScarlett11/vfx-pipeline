import sys

from asset_creation import create_asset
from asset_browser import get_assets
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import(QLabel, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QMainWindow, QApplication, QTabWidget, QWidget, QTableWidget, QTableWidgetItem, QHeaderView)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VFX Asset Pipeline")

        
        #create a tab widget
        tab = QTabWidget(self)

        #Asset Creation Tab
        asset_info = QWidget(self)
        layout = QVBoxLayout()
        asset_info.setLayout(layout)

        self.textbox = QLineEdit()
        self.textbox.setMaxLength(10)
        self.textbox.setPlaceholderText("Enter Asset Name")

        layout.addWidget(QLabel("Asset Name"))
        layout.addWidget(self.textbox)

        self.combobox = QComboBox()
        self.combobox.addItems(["Characters", "Props", "Environments"])

        layout.addWidget(QLabel("Asset Type"))
        layout.addWidget(self.combobox)

        self.comboboxLOD = QComboBox()
        self.comboboxLOD.addItems(["High", "Medium", "Low"])

        layout.addWidget(QLabel("Asset LOD"))
        layout.addWidget(self.comboboxLOD)

        self.Btn = QPushButton(text="Create Asset", parent=self)
        self.Btn.setFixedSize(100, 60)
        self.Btn.clicked.connect(self.create_asset)

        layout.addWidget(self.Btn)


        #Browser Tab
        browser = QWidget(self)
        layout = QVBoxLayout()
        browser.setLayout(layout)

        assets = get_assets()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setRowCount(len(assets))
        self.table.setHorizontalHeaderLabels(["Name", "Type", "Version", "Date Created"])

        for row_index, asset in enumerate(assets):
            self.table.setItem(row_index, 0, QTableWidgetItem(asset["Name"]))
            self.table.setItem(row_index, 1, QTableWidgetItem(asset["Type"]))
            self.table.setItem(row_index, 2, QTableWidgetItem(str(asset["Version"])))
            self.table.setItem(row_index, 3, QTableWidgetItem(asset["Date"]))
        
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setVisible(False)

        layout.addWidget(self.table)

    



        self.setCentralWidget(tab)

        tab.addTab(asset_info, 'Create an Asset')
        tab.addTab(browser, 'Asset Browser')

    def create_asset(self):
        create_asset(self.textbox.text(), self.combobox.currentText(), self.comboboxLOD.currentText())

    def get_assets(self):
        get_assets(self.textbox.text(), self.combobox.currentText(), self.comboboxLOD.currentText())




app = QApplication(sys.argv)

window = MainWindow()
window.setMinimumWidth(400)
window.show()
sys.exit(app.exec())