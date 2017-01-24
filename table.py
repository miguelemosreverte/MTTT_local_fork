# -*- coding: utf-8 -*-

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

    def setmydata(self):
        horHeaders = []
        for y, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for x, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(x, y, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

    def create_bilingual_table(self,data):
        horHeaders = []
        data["unmodified_target"] = data["target"]
        for key in data.keys():
            if key == "source": y = 0
            if key == "unmodified_target": y = 1
            if key == "target": y = 2
            horHeaders.insert(y,key)
            for x, item in enumerate(data[key]):
                #newitem = QTableWidgetItem(item)
                tableItem = QTextEdit()
                tableItem.setText(item)
                if key != "target": tableItem.setReadOnly(True)
                tableItem.mousePressEvent =  (lambda event= tableItem, tableItem= tableItem,x=x, y=y: self.tableItemSelectedCallback(event, tableItem,x,y))
                tableItem.textChanged.connect(lambda tableItem= tableItem,x=x, y=y: self.tableItemChangedCallback(tableItem,x,y))
                #tableItem.mousePressEvent.connect(lambda tableItem= tableItem,x=x, y=y: self.tableItemSelectedCallback(tableItem,x,y))
                self.setCellWidget(x,y, tableItem)
        self.setHorizontalHeaderLabels(horHeaders)

    def create_monolingual_table(self,data):
        horHeaders = []
        for y in range (0,2):
            if y == 0: key = "source"
            if y == 1: key = "target"
            horHeaders.append(key)
            for x, item in enumerate(data["target"]):
                #newitem = QTableWidgetItem(item)
                tableItem = QTextEdit()
                tableItem.setFixedWidth(250)
                tableItem.setText(item)
                if y == 0: tableItem.setReadOnly(True)
                tableItem.mousePressEvent =  (lambda event= tableItem, tableItem= tableItem,x=x, y=y: self.tableItemSelectedCallback(event, tableItem,x,y))
                tableItem.textChanged.connect(lambda tableItem= tableItem,x=x, y=y: self.tableItemChangedCallback(tableItem,x,y))
                #tableItem.mousePressEvent.connect(lambda tableItem= tableItem,x=x, y=y: self.tableItemSelectedCallback(tableItem,x,y))
                self.setCellWidget(x,y, tableItem)
        self.setHorizontalHeaderLabels(horHeaders)


    def set_post_editing_table_data(self, data, bilingual = False):
        self.clear()
        if bilingual: self.create_bilingual_table(data)
        else: self.create_monolingual_table(data)

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setColumnHidden(2, not bilingual)
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setStretchLastSection(True)

    def set_differences_table_data(self, data):
        horHeaders = []
        for key in data.keys():
            if key == "source": y = 0
            if key == "target": y = 1
            horHeaders.insert(y,key)
            for x, item in enumerate(data[key]):
                #newitem = QTableWidgetItem(item)
                tableItem = QTextEdit()
                #tableItem.setFixedWidth(250)
                tableItem.setText(item)
                if key != "target": tableItem.setReadOnly(True)
                tableItem.mousePressEvent =  (lambda event= tableItem, tableItem= tableItem,x=x, y=y: self.tableItemSelectedCallback(event, tableItem,x,y))
                tableItem.textChanged.connect(lambda tableItem= tableItem,x=x, y=y: self.tableItemChangedCallback(tableItem,x,y))
                self.setCellWidget(x,y, tableItem)

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setHorizontalHeaderLabels(horHeaders)
        self.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setStretchLastSection(True)

    def changeColorOfItem(self,X,Y):
        self.item(X,Y).setBackground(QColor(100,100,150))

def main(args):
    app = QApplication(args)
    table = MyTable(data, 5, 3)
    table.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)
