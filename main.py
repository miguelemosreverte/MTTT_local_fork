# -*- coding: utf-8 -*-

from PyQt4.QtGui import QApplication

import os
import sys

from mainWindow import MainWindow
from datamodel import DataModel

if __name__ == "__main__":


    app = QApplication(sys.argv)
    workdir = os.path.join(os.path.join(os.path.expanduser('~'), 'mosesgui'))
    if not os.path.exists(workdir):
        os.makedirs(workdir)
    dm = DataModel(filename=os.path.join(workdir, "models.sqlite"))

    MainWindow = MainWindow(dm=dm)
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
