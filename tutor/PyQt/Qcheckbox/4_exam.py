import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout,QCheckBox, QHBoxLayout
from PyQt5 import Qt,QtCore


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Checkbox in Table'
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480        
        self.numRow = 5
        self.numCol = 5

        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)        
        self.createTable()               
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()
     

    def createTable(self):       
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.numRow)        
        self.tableWidget.setColumnCount(self.numCol)                
        self.tableWidget.move(0,0)        

        self.InsertTable()
   

    def InsertTable(self):                    
    
        self.checkBoxList = []
        for i in range(self.numRow):
            ckbox = QCheckBox()
            self.checkBoxList.append(ckbox)

        for i in range(self.numRow):              
            cellWidget = QWidget()
            layoutCB = QHBoxLayout(cellWidget)
            layoutCB.addWidget(self.checkBoxList[i])
            layoutCB.setAlignment(QtCore.Qt.AlignCenter)            
            layoutCB.setContentsMargins(0,0,0,0)
            cellWidget.setLayout(layoutCB)

            self.tableWidget.setCellWidget(i,0,cellWidget)            
            
        
        self.tableWidget.move(0,0)                 

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableWidget()
    sys.exit(app.exec_())