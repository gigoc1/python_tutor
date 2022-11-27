from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

class MyHeader(QHeaderView):

    isOn = False

    def __init__(self, orientation, parent=None):
        QHeaderView.__init__(self, orientation, parent)

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        QHeaderView.paintSection(self, painter, rect, logicalIndex)
        painter.restore()

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(10, 10, 10, 10)
            if self.isOn:
                option.state = QStyle.State_On
            else:
                option.state = QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        self.isOn = not self.isOn
        self.updateSection(0)
        QHeaderView.mousePressEvent(self, event)

class MyTable(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self, 3, 3)

        myHeader = QCheckableHeader(Qt.Horizontal, self)
        self.setHorizontalHeader(myHeader)

class QCheckableHeader(QHeaderView):

    def __init__(self, orientation, parent=None):
        QHeaderView.__init__(self, orientation, parent)
        self.lisCheckboxes = []
        self.sectionCountChanged.connect(self.onSectionCountChanged)

    def paintSection(self, painter, rect, logicalIndex):
        print("paintSection", logicalIndex)
        painter.save()
        QHeaderView.paintSection(self, painter, rect, logicalIndex)
        painter.restore()
        painter.save()
        painter.translate(rect.topLeft())

        option = QStyleOptionButton()
        option.rect = QRect(10, 10, 10, 10)
        if (len(self.lisCheckboxes) != self.count()):
            self.onSectionCountChanged(len(self.lisCheckboxes), self.count())

        if self.lisCheckboxes[logicalIndex]:
            option.state = QStyle.State_On
        else:
            option.state = QStyle.State_Off
        self.style().drawControl(QStyle.CE_CheckBox, option, painter)
        painter.restore()

    def mousePressEvent(self, event):

        iIdx = self.logicalIndexAt(event.pos())
        self.lisCheckboxes[iIdx] = not self.lisCheckboxes[iIdx]
        self.updateSection(iIdx)
        QHeaderView.mousePressEvent(self, event)

    # @QtCore.Slot()
    def onSectionCountChanged(self, oldCount,  newCount):
        if newCount > oldCount:
            for i in range(newCount - oldCount):
                self.lisCheckboxes.append(False)
        else:
            self.lisCheckboxes = self.lisCheckboxes[0:newCount]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
    myTable.show()
    sys.exit(app.exec_())