# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\work\eric4workspace\MosesGUI\mainWindow.ui'
#
# Created: Thu Jul 11 13:38:46 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from table import MyTable

import sys
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

_fromUtf8 = getattr(QtCore.QString, 'fromUtf8', lambda s: s)


def _translate(context, text, disambig):
    return QtGui.QApplication.translate(
        context, text, disambig,
        getattr(
            QtGui.QApplication, 'UnicodeUTF8',
            QtCore.QCoreApplication.Encoding))

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.modified_table_items_coordinates = []
        self.lastChangedTableItemCoordinates = (-1,-1)

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(705, 491)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/moses.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralWidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.background_color_palette = QtGui.QPalette()
        self.background_color_palette.setColor(QtGui.QPalette.Background,QColor("#edf2f6"))

        self.initialize_preprocessing_tab()
        self.initialize_tab_machine_translation()
        self.initialize_training_tab()
        self.initialize_tab_evaluation()
        self.initialize_post_editing_tab()
        self.initialize_tab_statistics()
        self.initialize_tab_differences()


        self.tabWidget.addTab(self.tab_corpus_preparation, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_training, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_machine_translation, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_evaluation, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_post_editing, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_differences, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_statistics, _fromUtf8(""))


        self.verticalLayout_3.addWidget(self.tabWidget)
        self.labelInfo = QtGui.QLabel(self.centralWidget)
        self.labelInfo.setTextFormat(QtCore.Qt.AutoText)
        self.labelInfo.setAlignment(
            QtCore.Qt.AlignRight |
            QtCore.Qt.AlignTrailing |
            QtCore.Qt.AlignVCenter)
        self.labelInfo.setObjectName(_fromUtf8("labelInfo"))
        self.verticalLayout_3.addWidget(self.labelInfo)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def choose_language(self, tab, source_or_target, language):
        print language
        if tab == "preprocessing":
            if source_or_target == "source":
                self.preprocessing_source_language = language
            elif source_or_target == "target":
                self.preprocessing_target_language = language
    def initialize_tab_differences(self):
        self.tab_differences = QtGui.QWidget()
        self.tab_differences.setAutoFillBackground(True)
        self.tab_differences.setPalette(self.background_color_palette)
        self.tab_differences.setObjectName(_fromUtf8("tab_differences"))
        verticalLayout_2 = QtGui.QVBoxLayout(self.tab_differences)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        groupBox= QtGui.QGroupBox(self.tab_differences)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))



        verticalLayout_2.addWidget(groupBox)
        splitter = QtGui.QSplitter(self.tab_differences)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))

        splitter2 = QtGui.QSplitter(self.tab_differences)
        splitter2.setOrientation(QtCore.Qt.Vertical)
        splitter2.setObjectName(_fromUtf8("splitter2"))

        self.table_differences= MyTable({'col1':[], 'col2':[]},self.on_tableItemDifferencestextChanged,self.on_tableItemDifferences_selected,10,2)
        splitter.addWidget(self.table_differences)
        verticalLayout_2.addWidget(splitter)
        verticalLayout_2.setStretch(1, 8)
        self.tab_differences.setAutoFillBackground(True)
        self.tab_differences.setObjectName(_fromUtf8("tab_differences"))

        self.search_table_differences= MyTable({'Search Results':[]},self.on_tableItemDifferencestextChanged,self.on_tableItemDifferences_selected,10,1)
        splitter.addWidget(self.search_table_differences)
        verticalLayout_2.addWidget(splitter2)
        verticalLayout_2.setStretch(1, 8)
        self.tab_differences.setAutoFillBackground(True)
        self.tab_differences.setObjectName(_fromUtf8("tab_differences"))
        #edit_target_differences
        self.edit_search_differences = QtGui.QLineEdit(groupBox)
        self.edit_search_differences.setReadOnly(False)
        self.edit_search_differences.setObjectName(_fromUtf8("edit_search_differences"))
        gridLayout.addWidget(self.edit_search_differences, 5, 3, 1, 1)

        self.btnBackDifferences = QtGui.QPushButton(groupBox)
        self.btnBackDifferences.setEnabled(True)
        self.btnBackDifferences.setMinimumSize(QtCore.QSize(120, 30))
        self.btnBackDifferences.setFlat(False)
        self.btnBackDifferences.setText(_translate("Dialog", "Back", None))
        self.btnBackDifferences.setObjectName(_fromUtf8("btnBackDifferences"))
        gridLayout.addWidget(self.btnBackDifferences, 1, 1, 1, 1)
        self.btnBackDifferences.hide()

        self.btnNextDifferences = QtGui.QPushButton(groupBox)
        self.btnNextDifferences.setEnabled(True)
        self.btnNextDifferences.setMaximumSize(QtCore.QSize(120, 30))
        self.btnNextDifferences.setFlat(False)
        self.btnNextDifferences.setText(_translate("Dialog", "Next", None))
        self.btnNextDifferences.setObjectName(_fromUtf8("btnNextDifferences"))
        gridLayout.addWidget(self.btnNextDifferences, 1, 2, 1, 1)
        self.btnNextDifferences.hide()

        self.btnSearchDifferences = QtGui.QPushButton(groupBox)
        self.btnSearchDifferences.setEnabled(True)
        self.btnSearchDifferences.setFlat(False)
        self.btnSearchDifferences.setObjectName(_fromUtf8("btnSearchDifferences"))
        gridLayout.addWidget(self.btnSearchDifferences, 1, 3, 1, 1)
        self.toggled_search_differences = True
        self.search_table_differences.hide()
        self.edit_search_differences.hide()

        self.btnSearchDifferences.setText(_translate("Dialog", "Search", None))

    def initialize_tab_statistics(self):
        self.tab_statistics = QtGui.QWidget()
        self.tab_statistics.setAutoFillBackground(True)
        self.tab_statistics.setPalette(self.background_color_palette)
        self.tab_statistics.setObjectName(_fromUtf8("tab_statistics"))
        verticalLayout_2 = QtGui.QVBoxLayout(self.tab_statistics)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        splitter = QtGui.QSplitter(self.tab_statistics)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))
        verticalLayout_2.addWidget(splitter)
        verticalLayout_2.setStretch(0, 2)
        verticalLayout_2.setStretch(1, 8)
        self.tab_statistics.setAutoFillBackground(True)
        self.tab_statistics.setObjectName(_fromUtf8("tab_statistics"))
        self.HTMLview = QWebView(splitter)

        self.label_source_evaluation_tab.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.label_target_evaluation_tab.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.label_output_dir_evaluation_tab.setText(_translate("MainWindow", "Output text", None))
        self.btn_output_dir_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.btnEvaluation.setText(_translate("MainWindow", "Start Evaluation", None))

    def initialize_tab_evaluation(self):
        self.tab_evaluation = QtGui.QWidget()
        self.tab_evaluation.setAutoFillBackground(True)
        self.tab_evaluation.setPalette(self.background_color_palette)
        self.tab_evaluation.setObjectName(_fromUtf8("tab_evaluation"))
        verticalLayout_2 = QtGui.QVBoxLayout(self.tab_evaluation)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        groupBox_evaluation = QtGui.QGroupBox(self.tab_evaluation)
        groupBox_evaluation.setObjectName(_fromUtf8("groupBox_evaluation"))
        groupBox_evaluation.setTitle(_translate("MainWindow", "Evaluation", None))
        gridLayout = QtGui.QGridLayout(groupBox_evaluation)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #label_source_evaluation_tab
        self.label_source_evaluation_tab = QtGui.QLabel(groupBox_evaluation)
        self.label_source_evaluation_tab.setObjectName(_fromUtf8("label_source_evaluation_tab"))
        gridLayout.addWidget(self.label_source_evaluation_tab, 1, 1, 1, 1)
        #btn_source_evaluation_tab
        self.btn_source_evaluation_tab = QtGui.QPushButton(groupBox_evaluation)
        self.btn_source_evaluation_tab.setObjectName(_fromUtf8("btn_source_evaluation_tab"))
        gridLayout.addWidget(self.btn_source_evaluation_tab, 1, 3, 1, 1)
        #edit_source_evaluation_tab
        self.edit_source_evaluation_tab = QtGui.QLineEdit(groupBox_evaluation)
        self.edit_source_evaluation_tab.setReadOnly(True)
        self.edit_source_evaluation_tab.setObjectName(_fromUtf8("edit_source_evaluation_tab"))
        gridLayout.addWidget(self.edit_source_evaluation_tab, 1, 2, 1, 1)

        #label_target_evaluation_tab
        self.label_target_evaluation_tab = QtGui.QLabel(groupBox_evaluation)
        self.label_target_evaluation_tab.setObjectName(_fromUtf8("label_target_evaluation_tab"))
        gridLayout.addWidget(self.label_target_evaluation_tab, 2, 1, 1, 1)
        #btn_target_evaluation_tab
        self.btn_target_evaluation_tab = QtGui.QPushButton(groupBox_evaluation)
        self.btn_target_evaluation_tab.setObjectName(_fromUtf8("btn_target_evaluation_tab"))
        gridLayout.addWidget(self.btn_target_evaluation_tab, 2, 3, 1, 1)
        #edit_target_evaluation_tab
        self.edit_target_evaluation_tab = QtGui.QLineEdit(groupBox_evaluation)
        self.edit_target_evaluation_tab.setReadOnly(True)
        self.edit_target_evaluation_tab.setObjectName(_fromUtf8("edit_target_evaluation_tab"))
        gridLayout.addWidget(self.edit_target_evaluation_tab, 2, 2, 1, 1)

        #label_output_dir_evaluation_tab
        self.label_output_dir_evaluation_tab = QtGui.QLabel(groupBox_evaluation)
        self.label_output_dir_evaluation_tab.setObjectName(_fromUtf8("label_output_dir_evaluation_tab"))
        gridLayout.addWidget(self.label_output_dir_evaluation_tab, 3, 1, 1, 1)
        #btn_output_dir_evaluation_tab
        self.btn_output_dir_evaluation_tab = QtGui.QPushButton(groupBox_evaluation)
        self.btn_output_dir_evaluation_tab.setObjectName(_fromUtf8("btn_output_dir_evaluation_tab"))
        gridLayout.addWidget(self.btn_output_dir_evaluation_tab, 3, 3, 1, 1)
        #edit_output_evaluation_tab
        self.edit_output_evaluation_tab = QtGui.QLineEdit(groupBox_evaluation)
        self.edit_output_evaluation_tab.setReadOnly(True)
        self.edit_output_evaluation_tab.setObjectName(_fromUtf8("edit_output_evaluation_tab"))
        gridLayout.addWidget(self.edit_output_evaluation_tab, 3, 2, 1, 1)

        verticalLayout_2.addWidget(groupBox_evaluation)
        splitter = QtGui.QSplitter(self.tab_evaluation)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))
        self.results_evaluation = QtGui.QTextEdit(splitter)
        self.results_evaluation.setObjectName(_fromUtf8("results_evaluation"))
        verticalLayout_2.addWidget(splitter)
        verticalLayout_2.setStretch(0, 2)
        verticalLayout_2.setStretch(1, 8)
        self.tab_evaluation.setAutoFillBackground(True)
        self.tab_evaluation.setObjectName(_fromUtf8("tab_evaluation"))

        #btnEvaluation
        self.btnEvaluation = QtGui.QPushButton(groupBox_evaluation)
        self.btnEvaluation.setEnabled(True)
        self.btnEvaluation.setMinimumSize(QtCore.QSize(120, 30))
        self.btnEvaluation.setFlat(False)
        self.btnEvaluation.setObjectName(_fromUtf8("btnEvaluation"))
        gridLayout.addWidget(self.btnEvaluation, 4, 1, 1, 8)

        self.btn_check_WER = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_WER.setEnabled(True)
        self.btn_check_WER.setText("WER")
        self.btn_check_WER.setObjectName(_fromUtf8("btn_check_WER"))
        gridLayout.addWidget(self.btn_check_WER, 1, 5, 1, 1)

        self.btn_check_PER = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_PER.setEnabled(True)
        self.btn_check_PER.setText("PER")
        self.btn_check_PER.setObjectName(_fromUtf8("btn_check_PER"))
        gridLayout.addWidget(self.btn_check_PER, 1, 6, 1, 1)

        self.btn_check_HTER = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_HTER.setEnabled(True)
        self.btn_check_HTER.setText("HTER")
        self.btn_check_HTER.setObjectName(_fromUtf8("btn_check_HTER"))
        gridLayout.addWidget(self.btn_check_HTER, 1, 7, 1, 1)


        self.btn_check_GTM = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_GTM.setEnabled(True)
        self.btn_check_GTM.setText("GTM")
        self.btn_check_GTM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_GTM.setObjectName(_fromUtf8("btn_check_GTM"))
        gridLayout.addWidget(self.btn_check_GTM, 1, 8, 1, 1)


        self.btn_check_BLEU = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_BLEU.setEnabled(True)
        self.btn_check_BLEU.setText("BLEU")
        self.btn_check_BLEU.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU.setObjectName(_fromUtf8("btn_check_BLEU"))
        gridLayout.addWidget(self.btn_check_BLEU, 2, 5, 1, 1)

        self.btn_check_BLEU2GRAM = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_BLEU2GRAM.setEnabled(True)
        self.btn_check_BLEU2GRAM.setText("BLEU2")
        self.btn_check_BLEU2GRAM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU2GRAM.setObjectName(_fromUtf8("btn_check_BLEU2GRAM"))
        gridLayout.addWidget(self.btn_check_BLEU2GRAM, 2, 6, 1, 1)


        self.btn_check_BLEU3GRAM = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_BLEU3GRAM.setEnabled(True)
        self.btn_check_BLEU3GRAM.setText("BLEU3")
        self.btn_check_BLEU3GRAM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU3GRAM.setObjectName(_fromUtf8("btn_check_BLEU3GRAM"))
        gridLayout.addWidget(self.btn_check_BLEU3GRAM, 2, 7, 1, 1)


        self.btn_check_BLEU4GRAM = QtGui.QCheckBox(groupBox_evaluation)
        self.btn_check_BLEU4GRAM.setEnabled(True)
        self.btn_check_BLEU4GRAM.setText("BLEU4")
        self.btn_check_BLEU4GRAM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU4GRAM.setObjectName(_fromUtf8("btn_check_BLEU4GRAM"))
        gridLayout.addWidget(self.btn_check_BLEU4GRAM, 2, 8, 1, 1)

        self.label_evaluation_checkboxes_explanation = QtGui.QLabel(groupBox_evaluation)
        self.label_evaluation_checkboxes_explanation.setObjectName(_fromUtf8("label_evaluation_checkboxes_explanation"))
        self.label_evaluation_checkboxes_explanation.setText("*BLUE returns the average of all the BLUE tests,\n and BLUE2 means BLUE2GRAM")
        gridLayout.addWidget(self.label_evaluation_checkboxes_explanation, 3, 5, 1, 4)

        self.label_source_evaluation_tab.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.label_target_evaluation_tab.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.label_output_dir_evaluation_tab.setText(_translate("MainWindow", "Output text", None))
        self.btn_output_dir_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.btnEvaluation.setText(_translate("MainWindow", "Start Evaluation", None))
        groupBox_evaluation.setTitle(_translate("MainWindow", "Evaluation", None))

    def initialize_tab_machine_translation(self):
        self.tab_machine_translation = QtGui.QWidget()
        self.tab_machine_translation.setAutoFillBackground(True)
        self.tab_machine_translation.setPalette(self.background_color_palette)
        self.tab_machine_translation.setObjectName(_fromUtf8("tab_machine_translation"))
        verticalLayout_2 = QtGui.QVBoxLayout(self.tab_machine_translation)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        groupBox= QtGui.QGroupBox(self.tab_machine_translation)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #label_source_machine_translation_tab
        self.label_source_machine_translation_tab = QtGui.QLabel(groupBox)
        self.label_source_machine_translation_tab.setObjectName(_fromUtf8("label_source_machine_translation_tab"))
        gridLayout.addWidget(self.label_source_machine_translation_tab, 1, 1, 1, 1)
        #btn_source_machine_translation_tab
        self.btn_source_machine_translation_tab = QtGui.QPushButton(groupBox)
        self.btn_source_machine_translation_tab.setObjectName(_fromUtf8("btn_source_machine_translation_tab"))
        gridLayout.addWidget(self.btn_source_machine_translation_tab, 1, 3, 1, 1)
        #edit_source_machine_translation_tab
        self.edit_source_machine_translation_tab = QtGui.QLineEdit(groupBox)
        self.edit_source_machine_translation_tab.setReadOnly(True)
        self.edit_source_machine_translation_tab.setObjectName(_fromUtf8("edit_source_machine_translation_tab"))
        gridLayout.addWidget(self.edit_source_machine_translation_tab, 1, 2, 1, 1)

        verticalLayout_2.addWidget(groupBox)
        splitter = QtGui.QSplitter(self.tab_machine_translation)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))
        self.results_machine_translation = QtGui.QTextEdit(splitter)
        self.results_machine_translation.setObjectName(_fromUtf8("results_machine_translation"))
        verticalLayout_2.addWidget(splitter)
        verticalLayout_2.setStretch(0, 2)
        verticalLayout_2.setStretch(1, 8)
        self.tab_machine_translation.setAutoFillBackground(True)
        self.tab_machine_translation.setObjectName(_fromUtf8("tab_machine_translation"))

        #btnMachineTranslation
        self.btnMachineTranslation = QtGui.QPushButton(groupBox)
        self.btnMachineTranslation.setEnabled(True)
        self.btnMachineTranslation.setMinimumSize(QtCore.QSize(120, 30))
        self.btnMachineTranslation.setFlat(False)
        self.btnMachineTranslation.setObjectName(_fromUtf8("btnMachineTranslation"))
        gridLayout.addWidget(self.btnMachineTranslation, 4, 1, 1, 4)

        self.label_source_machine_translation_tab.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_machine_translation_tab.setText(_translate("Dialog", "...", None))
        self.btnMachineTranslation.setText(_translate("MainWindow", "Start Machine Translation", None))

    def initialize_post_editing_tab(self):
        self.tab_post_editing = QtGui.QWidget()
        self.tab_post_editing.setAutoFillBackground(True)
        self.tab_post_editing.setPalette(self.background_color_palette)
        self.tab_post_editing.setObjectName(_fromUtf8("tab_post_editing"))
        verticalLayout_2 = QtGui.QVBoxLayout(self.tab_post_editing)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        groupBox= QtGui.QGroupBox(self.tab_post_editing)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #label_source_post_editing
        self.label_source_post_editing = QtGui.QLabel(groupBox)
        self.label_source_post_editing.setObjectName(_fromUtf8("label_source_post_editing"))
        gridLayout.addWidget(self.label_source_post_editing, 1, 1, 1, 1)
        #btn_source_post_editing
        self.btn_source_post_editing = QtGui.QPushButton(groupBox)
        self.btn_source_post_editing.setObjectName(_fromUtf8("btn_source_post_editing"))
        gridLayout.addWidget(self.btn_source_post_editing, 1, 3, 1, 1)
        #edit_source_post_editing
        self.edit_source_post_editing = QtGui.QLineEdit(groupBox)
        self.edit_source_post_editing.setReadOnly(True)
        self.edit_source_post_editing.setObjectName(_fromUtf8("edit_source_post_editing"))
        gridLayout.addWidget(self.edit_source_post_editing, 1, 2, 1, 1)

        #label_target_post_editing
        self.label_target_post_editing = QtGui.QLabel(groupBox)
        self.label_target_post_editing.setObjectName(_fromUtf8("label_target_post_editing"))
        gridLayout.addWidget(self.label_target_post_editing, 2, 1, 1, 1)
        #btn_target_post_editing
        self.btn_target_post_editing = QtGui.QPushButton(groupBox)
        self.btn_target_post_editing.setObjectName(_fromUtf8("btn_target_post_editing"))
        gridLayout.addWidget(self.btn_target_post_editing, 2, 3, 1, 1)
        #edit_target_post_editing
        self.edit_target_post_editing = QtGui.QLineEdit(groupBox)
        self.edit_target_post_editing.setReadOnly(True)
        self.edit_target_post_editing.setObjectName(_fromUtf8("edit_target_post_editing"))
        gridLayout.addWidget(self.edit_target_post_editing, 2, 2, 1, 1)

        verticalLayout_2.addWidget(groupBox)
        splitter = QtGui.QSplitter(self.tab_post_editing)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))

        splitter2 = QtGui.QSplitter(self.tab_post_editing)
        splitter2.setOrientation(QtCore.Qt.Vertical)
        splitter2.setObjectName(_fromUtf8("splitter2"))

        self.table_post_editing= MyTable({'col1':[], 'col2':[]},self.on_tableItemPostEditing_textChanged,self.on_tableItemPostEdition_selected,10,2)
        splitter.addWidget(self.table_post_editing)
        verticalLayout_2.addWidget(splitter)
        verticalLayout_2.setStretch(1, 8)
        self.tab_post_editing.setAutoFillBackground(True)
        self.tab_post_editing.setObjectName(_fromUtf8("tab_post_editing"))

        self.search_table_post_editing= MyTable({'Search Results':[]},self.on_tableItemPostEditing_textChanged,self.on_tableItemPostEdition_selected,10,1)
        splitter.addWidget(self.search_table_post_editing)
        verticalLayout_2.addWidget(splitter2)
        verticalLayout_2.setStretch(1, 8)
        self.tab_post_editing.setAutoFillBackground(True)
        self.tab_post_editing.setObjectName(_fromUtf8("tab_post_editing"))
        #edit_target_post_editing
        self.edit_search_post_editing = QtGui.QLineEdit(groupBox)
        self.edit_search_post_editing.setReadOnly(False)
        self.edit_search_post_editing.setObjectName(_fromUtf8("edit_search_post_editing"))
        gridLayout.addWidget(self.edit_search_post_editing, 5, 3, 1, 1)

        self.btnSearchPostEditing = QtGui.QPushButton(groupBox)
        self.btnSearchPostEditing.setEnabled(True)
        self.btnSearchPostEditing.setFlat(False)
        self.btnSearchPostEditing.setObjectName(_fromUtf8("btnSearchPostEditing"))
        gridLayout.addWidget(self.btnSearchPostEditing, 4, 3, 1, 1)
        self.toggled_search_post_editing = True
        self.search_table_post_editing.hide()
        self.edit_search_post_editing.hide()

        self.btnStartPostEditing = QtGui.QPushButton(groupBox)
        self.btnStartPostEditing.setEnabled(True)
        self.btnStartPostEditing.setMinimumSize(QtCore.QSize(120, 30))
        self.btnStartPostEditing.setFlat(False)
        self.btnStartPostEditing.setText(_translate("Dialog", "Start Post-Editing", None))
        self.btnStartPostEditing.setObjectName(_fromUtf8("btnStartPostEditing"))
        gridLayout.addWidget(self.btnStartPostEditing, 4, 1, 1, 2)
        self.table_post_editing.hide()

        self.btnBackPostEditing = QtGui.QPushButton(groupBox)
        self.btnBackPostEditing.setEnabled(True)
        self.btnBackPostEditing.setMinimumSize(QtCore.QSize(120, 30))
        self.btnBackPostEditing.setFlat(False)
        self.btnBackPostEditing.setText(_translate("Dialog", "Back", None))
        self.btnBackPostEditing.setObjectName(_fromUtf8("btnBackPostEditing"))
        gridLayout.addWidget(self.btnBackPostEditing, 5, 1, 1, 1)
        self.btnBackPostEditing.hide()

        self.btnNextPostEditing = QtGui.QPushButton(groupBox)
        self.btnNextPostEditing.setEnabled(True)
        self.btnNextPostEditing.setMaximumSize(QtCore.QSize(120, 30))
        self.btnNextPostEditing.setFlat(False)
        self.btnNextPostEditing.setText(_translate("Dialog", "Next", None))
        self.btnNextPostEditing.setObjectName(_fromUtf8("btnNextPostEditing"))
        gridLayout.addWidget(self.btnNextPostEditing, 5, 2, 1, 1)
        self.btnNextPostEditing.hide()

        self.btnSave = QtGui.QPushButton(groupBox)
        self.btnSave.setEnabled(True)
        self.btnSave.setMaximumSize(QtCore.QSize(120, 30))
        self.btnSave.setFlat(False)
        self.btnSave.setText(_translate("Dialog", "Save", None))
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        gridLayout.addWidget(self.btnSave, 1, 4, 1, 1)
        self.btnSave.hide()

        self.btnDiff = QtGui.QPushButton(groupBox)
        self.btnDiff.setEnabled(True)
        self.btnDiff.setMaximumSize(QtCore.QSize(120, 30))
        self.btnDiff.setFlat(False)
        self.btnDiff.setText(_translate("Dialog", "See changes", None))
        self.btnDiff.setObjectName(_fromUtf8("btnDiff"))
        gridLayout.addWidget(self.btnDiff, 2, 4, 1, 1)
        self.btnDiff.hide()

        self.btnStats = QtGui.QPushButton(groupBox)
        self.btnStats.setEnabled(True)
        self.btnStats.setMaximumSize(QtCore.QSize(120, 30))
        self.btnStats.setFlat(False)
        self.btnStats.setText(_translate("Dialog", "See stats", None))
        self.btnStats.setObjectName(_fromUtf8("btnStats"))
        gridLayout.addWidget(self.btnStats, 4, 4, 1, 1)
        self.btnStats.hide()


        self.btnFirstStat = QtGui.QPushButton(groupBox)
        self.btnFirstStat.setEnabled(True)
        self.btnFirstStat.setMaximumSize(QtCore.QSize(120, 30))
        self.btnFirstStat.setFlat(False)
        self.btnFirstStat.setText(_translate("Dialog", "First Stat", None))
        self.btnFirstStat.setObjectName(_fromUtf8("btnFirstStat"))
        gridLayout.addWidget(self.btnFirstStat, 1, 5, 1, 1)
        self.btnFirstStat.hide()

        self.btnSecondStat = QtGui.QPushButton(groupBox)
        self.btnSecondStat.setEnabled(True)
        self.btnSecondStat.setMaximumSize(QtCore.QSize(120, 30))
        self.btnSecondStat.setFlat(False)
        self.btnSecondStat.setText(_translate("Dialog", "Second Stat", None))
        self.btnSecondStat.setObjectName(_fromUtf8("btnSecondStat"))
        gridLayout.addWidget(self.btnSecondStat, 2, 5, 1, 1)
        self.btnSecondStat.hide()

        self.btnThirdStat = QtGui.QPushButton(groupBox)
        self.btnThirdStat.setEnabled(True)
        self.btnThirdStat.setMaximumSize(QtCore.QSize(120, 30))
        self.btnThirdStat.setFlat(False)
        self.btnThirdStat.setText(_translate("Dialog", "Third Stat", None))
        self.btnThirdStat.setObjectName(_fromUtf8("btnThirdStat"))
        gridLayout.addWidget(self.btnThirdStat, 4, 5, 1, 1)
        self.btnThirdStat.hide()

        self.label_source_post_editing.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_post_editing.setText(_translate("Dialog", "...", None))
        self.label_target_post_editing.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_post_editing.setText(_translate("Dialog", "...", None))
        self.btnSearchPostEditing.setText(_translate("Dialog", "Search", None))

    def initialize_preprocessing_tab(self):
        self.tab_corpus_preparation = QtGui.QWidget()
        self.tab_corpus_preparation.setAutoFillBackground(True)
        self.tab_corpus_preparation.setPalette(self.background_color_palette)
        self.tab_corpus_preparation.setObjectName(_fromUtf8("tab_corpus_preparation"))
        verticalLayout_2 = QtGui.QVBoxLayout(self.tab_corpus_preparation)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))


        groupBox = QtGui.QGroupBox(self.tab_corpus_preparation)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        groupBox.setStyleSheet("""#groupBox
        {
        border: none;
        background-color: none;
        }""")
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))


        groupBox2 = QtGui.QGroupBox(groupBox)
        groupBox2.setObjectName(_fromUtf8("groupBox2"))
        groupBox2.setTitle(_translate("MainWindow", "Languages", None))
        gridLayout2 = QtGui.QGridLayout(groupBox2)
        gridLayout2.setObjectName(_fromUtf8("gridLayout2"))
        gridLayout.addWidget(groupBox2, 1, 0, 1, 1)


        groupBox3 = QtGui.QGroupBox(groupBox)
        groupBox3.setObjectName(_fromUtf8("groupBox3"))
        groupBox3.setTitle(_translate("MainWindow", "Translation Model", None))
        gridLayout3 = QtGui.QGridLayout(groupBox3)
        gridLayout3.setObjectName(_fromUtf8("gridLayout3"))
        gridLayout.addWidget(groupBox3, 1, 1, 1, 1)

        groupBox4 = QtGui.QGroupBox(groupBox)
        groupBox4.setObjectName(_fromUtf8("groupBox4"))
        groupBox4.setTitle(_translate("MainWindow", "Language Model", None))
        gridLayout4 = QtGui.QGridLayout(groupBox4)
        gridLayout4.setObjectName(_fromUtf8("gridLayout4"))
        gridLayout.addWidget(groupBox4, 2, 1, 1, 1)

        groupBox5 = QtGui.QGroupBox(groupBox)
        groupBox5.setObjectName(_fromUtf8("groupBox5"))
        groupBox5.setTitle(_translate("MainWindow", "Settings", None))
        gridLayout5 = QtGui.QGridLayout(groupBox5)
        gridLayout5.setObjectName(_fromUtf8("gridLayout5"))
        gridLayout.addWidget(groupBox5, 3, 1, 1, 1)

        groupBox6 = QtGui.QGroupBox(groupBox)
        groupBox6.setObjectName(_fromUtf8("groupBox6"))
        groupBox6.setTitle(_translate("MainWindow", "Results", None))
        gridLayout6 = QtGui.QGridLayout(groupBox6)
        gridLayout6.setObjectName(_fromUtf8("gridLayout6"))
        gridLayout.addWidget(groupBox6, 2, 0, 4, 1)


        #btn_choose_source_lang_preprocessing
        self.btn_choose_source_lang_preprocessing = QtGui.QPushButton('Source Language')
        menu = QtGui.QMenu()
        menu.addAction('EN', lambda: self.choose_language("preprocessing","source",'EN'))
        menu.addAction('FR', lambda: self.choose_language("preprocessing","source",'FR'))
        menu.addAction('DE', lambda: self.choose_language("preprocessing","source",'DE'))
        self.preprocessing_source_language = ""
        self.btn_choose_source_lang_preprocessing.setMenu(menu)
        gridLayout2.addWidget(self.btn_choose_source_lang_preprocessing, 1, 0, 1, 1)
        #btn_choose_target_lang_preprocessing
        self.btn_choose_target_lang_preprocessing = QtGui.QPushButton('Target Language')
        menu = QtGui.QMenu()
        menu.addAction('EN', lambda: self.choose_language("preprocessing","target",'EN'))
        menu.addAction('FR', lambda: self.choose_language("preprocessing","target",'FR'))
        menu.addAction('DE', lambda: self.choose_language("preprocessing","target",'DE'))
        self.preprocessing_target_language = ""
        self.btn_choose_target_lang_preprocessing.setMenu(menu)
        gridLayout2.addWidget(self.btn_choose_target_lang_preprocessing, 2, 0, 1, 1)

        #label_source_preprocessing_tab
        self.label_source_preprocessing_tab = QtGui.QLabel(groupBox)
        self.label_source_preprocessing_tab.setObjectName(_fromUtf8("label_source_preprocessing_tab"))
        gridLayout3.addWidget(self.label_source_preprocessing_tab, 1, 1, 1, 1)
        #btn_source_preprocessing_tab
        self.btn_source_preprocessing_tab = QtGui.QPushButton(groupBox)
        self.btn_source_preprocessing_tab.setObjectName(_fromUtf8("btn_source_preprocessing_tab"))
        gridLayout3.addWidget(self.btn_source_preprocessing_tab, 1, 3, 1, 1)
        #edit_source_preprocessing_tab
        self.edit_source_preprocessing_tab = QtGui.QLineEdit(groupBox)
        self.edit_source_preprocessing_tab.setReadOnly(True)
        self.edit_source_preprocessing_tab.setObjectName(_fromUtf8("edit_source_preprocessing_tab"))
        gridLayout3.addWidget(self.edit_source_preprocessing_tab, 1, 2, 1, 1)

        #label_target_preprocessing_tab
        self.label_target_preprocessing_tab = QtGui.QLabel(groupBox)
        self.label_target_preprocessing_tab.setObjectName(_fromUtf8("label_target_preprocessing_tab"))
        gridLayout3.addWidget(self.label_target_preprocessing_tab, 2, 1, 1, 1)
        #btn_target_preprocessing_tab
        self.btn_target_preprocessing_tab = QtGui.QPushButton(groupBox)
        self.btn_target_preprocessing_tab.setObjectName(_fromUtf8("btn_target_preprocessing_tab"))
        gridLayout3.addWidget(self.btn_target_preprocessing_tab, 2, 3, 1, 1)
        #edit_target_preprocessing_tab
        self.edit_target_preprocessing_tab = QtGui.QLineEdit(groupBox)
        self.edit_target_preprocessing_tab.setReadOnly(True)
        self.edit_target_preprocessing_tab.setObjectName(_fromUtf8("edit_target_preprocessing_tab"))
        gridLayout3.addWidget(self.edit_target_preprocessing_tab, 2, 2, 1, 1)

        #label_lm_text_preprocessing_tab
        self.label_lm_text_preprocessing_tab = QtGui.QLabel(groupBox)
        self.label_lm_text_preprocessing_tab.setObjectName(_fromUtf8("label_lm_text_preprocessing_tab"))
        gridLayout4.addWidget(self.label_lm_text_preprocessing_tab, 3, 1, 1, 1)
        #btn_lm_text_preprocessing_tab
        self.btn_lm_text_preprocessing_tab = QtGui.QPushButton(groupBox)
        self.btn_lm_text_preprocessing_tab.setObjectName(_fromUtf8("btn_lm_text_preprocessing_tab"))
        gridLayout4.addWidget(self.btn_lm_text_preprocessing_tab, 3, 3, 1, 1)
        #edit_lm_text_preprocessing_tab
        self.edit_lm_text_preprocessing_tab = QtGui.QLineEdit(groupBox)
        self.edit_lm_text_preprocessing_tab.setReadOnly(True)
        self.edit_lm_text_preprocessing_tab.setObjectName(_fromUtf8("edit_lm_text_preprocessing_tab"))
        gridLayout4.addWidget(self.edit_lm_text_preprocessing_tab, 3, 2, 1, 1)

        #label_output_dir_preprocessing_tab
        self.label_output_dir_preprocessing_tab = QtGui.QLabel(groupBox)
        self.label_output_dir_preprocessing_tab.setObjectName(_fromUtf8("label_output_dir_preprocessing_tab"))
        gridLayout5.addWidget(self.label_output_dir_preprocessing_tab, 4, 1, 1, 1)
        #btn_output_dir_preprocessing_tab
        self.btn_output_dir_preprocessing_tab = QtGui.QPushButton(groupBox)
        self.btn_output_dir_preprocessing_tab.setObjectName(_fromUtf8("btn_output_dir_preprocessing_tab"))
        gridLayout5.addWidget(self.btn_output_dir_preprocessing_tab, 4, 3, 1, 1)
        #edit_output_preprocessing_tab
        self.edit_output_preprocessing_tab = QtGui.QLineEdit(groupBox)
        self.edit_output_preprocessing_tab.setReadOnly(True)
        self.edit_output_preprocessing_tab.setObjectName(_fromUtf8("edit_output_preprocessing_tab"))
        gridLayout5.addWidget(self.edit_output_preprocessing_tab, 4, 2, 1, 1)

        verticalLayout_2.addWidget(groupBox)
        splitter = QtGui.QSplitter(self.tab_corpus_preparation)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))

        self.results_preprocessing = QtGui.QTextEdit(groupBox)
        self.results_preprocessing.setObjectName(_fromUtf8("results_preprocessing"))
        gridLayout6.addWidget(self.results_preprocessing , 5, 1, 1, 1)

        verticalLayout_2.addWidget(splitter)
        verticalLayout_2.setStretch(0, 2)
        verticalLayout_2.setStretch(1, 8)

        self.tab_corpus_preparation.setAutoFillBackground(True)
        self.tab_corpus_preparation.setObjectName(_fromUtf8("tab_corpus_preparation"))

        #btnPreProccess
        self.btnPreProccess = QtGui.QPushButton(groupBox)
        self.btnPreProccess.setEnabled(True)
        self.btnPreProccess.setMinimumSize(QtCore.QSize(120, 30))
        self.btnPreProccess.setFlat(False)
        self.btnPreProccess.setObjectName(_fromUtf8("btnPreProccess"))
        gridLayout.addWidget(self.btnPreProccess, 5, 1, 1, 1)

        self.label_source_preprocessing_tab.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_preprocessing_tab.setText(_translate("Dialog", "...", None))
        self.label_target_preprocessing_tab.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_preprocessing_tab.setText(_translate("Dialog", "...", None))
        self.label_lm_text_preprocessing_tab.setText(_translate("MainWindow", "Language Model", None))
        self.btn_lm_text_preprocessing_tab.setText(_translate("Dialog", "...", None))
        self.label_output_dir_preprocessing_tab.setText(_translate("MainWindow", "Output Directory", None))
        self.btn_output_dir_preprocessing_tab.setText(_translate("Dialog", "...", None))
        self.btnPreProccess.setText(_translate("MainWindow", "Start corpus preprocessing", None))

    def initialize_training_tab(self):
        self.tab_training = QtGui.QWidget()
        self.tab_training.setAutoFillBackground(True)
        self.tab_training.setPalette(self.background_color_palette)
        self.tab_training.setObjectName(_fromUtf8("tab_training"))
        verticalLayout_2 = QtGui.QVBoxLayout(self.tab_training)
        verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        groupBox = QtGui.QGroupBox(self.tab_training)
        groupBox.setObjectName(_fromUtf8("groupBox"))
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName(_fromUtf8("gridLayout"))
        verticalLayout_2.addWidget(groupBox)
        splitter = QtGui.QSplitter(self.tab_training)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName(_fromUtf8("splitter"))
        self.results_training = QtGui.QTextEdit(splitter)
        self.results_training.setObjectName(_fromUtf8("results_training"))
        verticalLayout_2.addWidget(splitter)
        verticalLayout_2.setStretch(0, 2)
        verticalLayout_2.setStretch(1, 8)
        self.tab_training.setAutoFillBackground(True)
        self.tab_training.setObjectName(_fromUtf8("tab_training"))
        self.btnTraining = QtGui.QPushButton(groupBox)
        self.btnTraining.setEnabled(True)
        self.btnTraining.setMinimumSize(QtCore.QSize(120, 30))
        self.btnTraining.setFlat(False)
        self.btnTraining.setObjectName(_fromUtf8("btnTraining"))
        gridLayout.addWidget(self.btnTraining, 4, 1, 1, 1)

        self.btnTraining.setText(_translate("MainWindow", "Start Training", None))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Translators Training Tool", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_corpus_preparation), _translate("MainWindow", "Corpus Preparation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_training), _translate("MainWindow", "Training", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), _translate("MainWindow", "Evaluation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_machine_translation), _translate("MainWindow", "Machine Translation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_post_editing), _translate("MainWindow", "Post Edition", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_differences), _translate("MainWindow", "Differences", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_statistics), _translate("MainWindow", "Statistics", None))

        self.tabWidget.setTabEnabled(5,False)
        self.tabWidget.setTabEnabled(6,False)
        self.labelInfo.setText(_translate("MainWindow", "<qt><a href=\"www\">Credits and Support</a></qt>", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
