#reference: https://learndataanalysis.org/qcheckbox-select-all-select-none-pyqt5-tutorial/
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Select All/Select None')
        self.window_width, self.window_height = 600, 200
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.checkBoxAll = QCheckBox('Select All')
        self.checkBoxAll.setChecked(False)
        self.checkBoxAll.stateChanged.connect(self.on_stateChanged)
        layout.addWidget(self.checkBoxAll)

        self.checkBoxA = QCheckBox('Select A')
        self.checkBoxB = QCheckBox('Select B')
        self.checkBoxC = QCheckBox('Select C')

        self.checkBoxes = [self.checkBoxA, self.checkBoxB, self.checkBoxC]
        for checkBox in self.checkBoxes:
            layout.addWidget(checkBox)

    def on_stateChanged(self, state):
        for checkBox in self.checkBoxes:
            checkBox.setCheckState(state)

if __name__ == '__main__':
    # don't auto scale.
    QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 30px;
        }
    ''')
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')