# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication

import os
import sys

from mainWindow import MainWindow
from datamodel import DataModel

if __name__ == "__main__":


    app = QApplication(sys.argv)

    MainWindow = MainWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
