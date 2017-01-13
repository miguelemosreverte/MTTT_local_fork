import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

data2 = {'col1':['1','2','3'], 'col2':['a','a','a']}

class MyTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.setAutoFillBackground(True)
        self.data = data
        #self.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.setEditTriggers(QAbstractItemView.AllEditTriggers)
        #self.resizeColumnsToContents()
        #self.resizeRowsToContents()

    def setmydata(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

    def setdata(self, data):
        horHeaders = []
        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                #newitem = QTableWidgetItem(item)
                tableItem = QTextEdit()
                tableItem.setFixedWidth(250)
                tableItem.setText(item)
                self.setCellWidget(m,n, tableItem )
                #self.setItem(m, n, newitem)

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
