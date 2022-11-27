#reference: https://github.com/yjg30737/pyqt-checkbox-list-widget
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMainWindow, QCheckBox, QVBoxLayout, QWidget
from pyqt_checkbox_table_widget.checkBoxTableWidget import CheckBoxTableWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        allChkBox = QCheckBox('Check all')
        tableWidget = CheckBoxTableWidget()
        tableWidget.setRowCount(10)
        tableWidget.stretchEveryColumnExceptForCheckBox() # stretch every section of tablewidget except for check box section
        for i in range(tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter) # align
            item.setText(str(i)*5) # text sample
            tableWidget.setItem(i, 1, item)
        allChkBox.stateChanged.connect(tableWidget.toggleState) # if allChkBox is checked, tablewidget checkboxes will also be checked 

        lay = QVBoxLayout()
        lay.addWidget(allChkBox)
        lay.addWidget(tableWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()