import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyTable(QTableWidget):
    def __init__(self, data, tableItemChangedCallback,tableItemSelectedCallback,*args):
        QTableWidget.__init__(self, *args)
        self.tableItemChangedCallback = tableItemChangedCallback
        self.tableItemSelectedCallback = tableItemSelectedCallback
        self.setAutoFillBackground(True)
        self.data = data
        self.setmydata()
        self.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setmydata(self):
        horHeaders = []
        for y, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for x, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(x, y, newitem)
        self.setHorizontalHeaderLabels(horHeaders)
        
    def setdata(self, data):

        horHeaders = []
        for y, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for x, item in enumerate(data[key]):
                #newitem = QTableWidgetItem(item)
                tableItem = QTextEdit()
                tableItem.setFixedWidth(250)
                tableItem.setText(item)
                tableItem.mousePressEvent =  (lambda event= tableItem, tableItem= tableItem,x=x, y=y: self.tableItemSelectedCallback(event, tableItem,x,y))
                tableItem.textChanged.connect(lambda tableItem= tableItem,x=x, y=y: self.tableItemChangedCallback(tableItem,x,y))
                #tableItem.mousePressEvent.connect(lambda tableItem= tableItem,x=x, y=y: self.tableItemSelectedCallback(tableItem,x,y))
                self.setCellWidget(x,y, tableItem)

                #self.setItem(x, y, newitem)

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setHorizontalHeaderLabels(horHeaders)

    def changeColorOfItem(self,X,Y):
        self.item(X,Y).setBackground(QColor(100,100,150))

def main(args):
    app = QApplication(args)
    table = MyTable(data, 5, 3)
    table.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)
