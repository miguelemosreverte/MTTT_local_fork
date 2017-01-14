# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\work\eric4workspace\MosesGUI\mainWindow.ui'
#
# Created: Thu Jul 11 13:38:46 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from table import MyTable

_fromUtf8 = getattr(QtCore.QString, 'fromUtf8', lambda s: s)


def _translate(context, text, disambig):
    return QtGui.QApplication.translate(
        context, text, disambig,
        getattr(
            QtGui.QApplication, 'UnicodeUTF8',
            QtCore.QCoreApplication.Encoding))


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
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

        #BEGGINING OF tab_corpus_preparation
        self.tab_corpus_preparation = QtGui.QWidget()
        self.tab_corpus_preparation.setAutoFillBackground(True)
        self.tab_corpus_preparation.setObjectName(_fromUtf8("tab_corpus_preparation"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_corpus_preparation)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_corpus_preparation)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #btn_choose_source_lang_preprocessing
        self.btn_choose_source_lang_preprocessing = QtGui.QPushButton('Source Language')
        menu = QtGui.QMenu()
        menu.addAction('EN', lambda: self.choose_language("preprocessing","source",'EN'))
        menu.addAction('FR', lambda: self.choose_language("preprocessing","source",'FR'))
        menu.addAction('DE', lambda: self.choose_language("preprocessing","source",'DE'))
        self.preprocessing_source_language = ""
        self.btn_choose_source_lang_preprocessing.setMenu(menu)
        self.gridLayout.addWidget(self.btn_choose_source_lang_preprocessing, 1, 0, 1, 1)
        #label_source_preprocessing_tab
        self.label_source_preprocessing_tab = QtGui.QLabel(self.groupBox)
        self.label_source_preprocessing_tab.setObjectName(_fromUtf8("label_source_preprocessing_tab"))
        self.gridLayout.addWidget(self.label_source_preprocessing_tab, 1, 1, 1, 1)
        #btn_source_preprocessing_tab
        self.btn_source_preprocessing_tab = QtGui.QPushButton(self.groupBox)
        self.btn_source_preprocessing_tab.setObjectName(_fromUtf8("btn_source_preprocessing_tab"))
        self.gridLayout.addWidget(self.btn_source_preprocessing_tab, 1, 3, 1, 1)
        #edit_source_preprocessing_tab
        self.edit_source_preprocessing_tab = QtGui.QLineEdit(self.groupBox)
        self.edit_source_preprocessing_tab.setReadOnly(True)
        self.edit_source_preprocessing_tab.setObjectName(_fromUtf8("edit_source_preprocessing_tab"))
        self.gridLayout.addWidget(self.edit_source_preprocessing_tab, 1, 2, 1, 1)

        #btn_choose_target_lang_preprocessing
        self.btn_choose_target_lang_preprocessing = QtGui.QPushButton('Target Language')
        menu = QtGui.QMenu()
        menu.addAction('EN', lambda: self.choose_language("preprocessing","target",'EN'))
        menu.addAction('FR', lambda: self.choose_language("preprocessing","target",'FR'))
        menu.addAction('DE', lambda: self.choose_language("preprocessing","target",'DE'))
        self.preprocessing_target_language = ""
        self.btn_choose_target_lang_preprocessing.setMenu(menu)
        self.gridLayout.addWidget(self.btn_choose_target_lang_preprocessing, 2, 0, 1, 1)
        #label_target_preprocessing_tab
        self.label_target_preprocessing_tab = QtGui.QLabel(self.groupBox)
        self.label_target_preprocessing_tab.setObjectName(_fromUtf8("label_target_preprocessing_tab"))
        self.gridLayout.addWidget(self.label_target_preprocessing_tab, 2, 1, 1, 1)
        #btn_target_preprocessing_tab
        self.btn_target_preprocessing_tab = QtGui.QPushButton(self.groupBox)
        self.btn_target_preprocessing_tab.setObjectName(_fromUtf8("btn_target_preprocessing_tab"))
        self.gridLayout.addWidget(self.btn_target_preprocessing_tab, 2, 3, 1, 1)
        #edit_target_preprocessing_tab
        self.edit_target_preprocessing_tab = QtGui.QLineEdit(self.groupBox)
        self.edit_target_preprocessing_tab.setReadOnly(True)
        self.edit_target_preprocessing_tab.setObjectName(_fromUtf8("edit_target_preprocessing_tab"))
        self.gridLayout.addWidget(self.edit_target_preprocessing_tab, 2, 2, 1, 1)

        #label_output_dir_preprocessing_tab
        self.label_output_dir_preprocessing_tab = QtGui.QLabel(self.groupBox)
        self.label_output_dir_preprocessing_tab.setObjectName(_fromUtf8("label_output_dir_preprocessing_tab"))
        self.gridLayout.addWidget(self.label_output_dir_preprocessing_tab, 3, 1, 1, 1)
        #btn_output_dir_preprocessing_tab
        self.btn_output_dir_preprocessing_tab = QtGui.QPushButton(self.groupBox)
        self.btn_output_dir_preprocessing_tab.setObjectName(_fromUtf8("btn_output_dir_preprocessing_tab"))
        self.gridLayout.addWidget(self.btn_output_dir_preprocessing_tab, 3, 3, 1, 1)
        #edit_output_preprocessing_tab
        self.edit_output_preprocessing_tab = QtGui.QLineEdit(self.groupBox)
        self.edit_output_preprocessing_tab.setReadOnly(True)
        self.edit_output_preprocessing_tab.setObjectName(_fromUtf8("edit_output_preprocessing_tab"))
        self.gridLayout.addWidget(self.edit_output_preprocessing_tab, 3, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.groupBox)
        self.splitter = QtGui.QSplitter(self.tab_corpus_preparation)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.results_preprocessing = QtGui.QTextEdit(self.splitter)
        self.results_preprocessing.setObjectName(_fromUtf8("results_preprocessing"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 8)
        self.tab_corpus_preparation.setAutoFillBackground(True)
        self.tab_corpus_preparation.setObjectName(_fromUtf8("tab_corpus_preparation"))

        #btnPreProccess
        self.btnPreProccess = QtGui.QPushButton(self.groupBox)
        self.btnPreProccess.setEnabled(True)
        self.btnPreProccess.setMinimumSize(QtCore.QSize(120, 30))
        self.btnPreProccess.setFlat(False)
        self.btnPreProccess.setObjectName(_fromUtf8("btnPreProccess"))
        self.gridLayout.addWidget(self.btnPreProccess, 4, 1, 1, 1)

        #BEGGINING OF tab_training
        self.tab_training = QtGui.QWidget()
        self.tab_training.setAutoFillBackground(True)
        self.tab_training.setObjectName(_fromUtf8("tab_training"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_training)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox2 = QtGui.QGroupBox(self.tab_training)
        self.groupBox2.setObjectName(_fromUtf8("groupBox2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2.addWidget(self.groupBox2)
        self.splitter = QtGui.QSplitter(self.tab_training)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.results_training = QtGui.QTextEdit(self.splitter)
        self.results_training.setObjectName(_fromUtf8("results_training"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 8)
        self.tab_training.setAutoFillBackground(True)
        self.tab_training.setObjectName(_fromUtf8("tab_training"))
        self.btnTraining = QtGui.QPushButton(self.groupBox2)
        self.btnTraining.setEnabled(True)
        self.btnTraining.setMinimumSize(QtCore.QSize(120, 30))
        self.btnTraining.setFlat(False)
        self.btnTraining.setObjectName(_fromUtf8("btnTraining"))
        self.gridLayout.addWidget(self.btnTraining, 4, 1, 1, 1)

        #BEGGINING OF tab_machine_translation
        self.tab_machine_translation = QtGui.QWidget()
        self.tab_machine_translation.setAutoFillBackground(True)
        self.tab_machine_translation.setObjectName(_fromUtf8("tab_machine_translation"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_machine_translation)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_machine_translation)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #label_source_machine_translation_tab
        self.label_source_machine_translation_tab = QtGui.QLabel(self.groupBox)
        self.label_source_machine_translation_tab.setObjectName(_fromUtf8("label_source_machine_translation_tab"))
        self.gridLayout.addWidget(self.label_source_machine_translation_tab, 1, 1, 1, 1)
        #btn_source_machine_translation_tab
        self.btn_source_machine_translation_tab = QtGui.QPushButton(self.groupBox)
        self.btn_source_machine_translation_tab.setObjectName(_fromUtf8("btn_source_machine_translation_tab"))
        self.gridLayout.addWidget(self.btn_source_machine_translation_tab, 1, 3, 1, 1)
        #edit_source_machine_translation_tab
        self.edit_source_machine_translation_tab = QtGui.QLineEdit(self.groupBox)
        self.edit_source_machine_translation_tab.setReadOnly(True)
        self.edit_source_machine_translation_tab.setObjectName(_fromUtf8("edit_source_machine_translation_tab"))
        self.gridLayout.addWidget(self.edit_source_machine_translation_tab, 1, 2, 1, 1)

        #label_target_machine_translation_tab
        self.label_target_machine_translation_tab = QtGui.QLabel(self.groupBox)
        self.label_target_machine_translation_tab.setObjectName(_fromUtf8("label_target_machine_translation_tab"))
        self.gridLayout.addWidget(self.label_target_machine_translation_tab, 2, 1, 1, 1)
        #btn_target_machine_translation_tab
        self.btn_target_machine_translation_tab = QtGui.QPushButton(self.groupBox)
        self.btn_target_machine_translation_tab.setObjectName(_fromUtf8("btn_target_machine_translation_tab"))
        self.gridLayout.addWidget(self.btn_target_machine_translation_tab, 2, 3, 1, 1)
        #edit_target_machine_translation_tab
        self.edit_target_machine_translation_tab = QtGui.QLineEdit(self.groupBox)
        self.edit_target_machine_translation_tab.setReadOnly(True)
        self.edit_target_machine_translation_tab.setObjectName(_fromUtf8("edit_target_machine_translation_tab"))
        self.gridLayout.addWidget(self.edit_target_machine_translation_tab, 2, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.groupBox)
        self.splitter = QtGui.QSplitter(self.tab_machine_translation)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.results_evaluation = QtGui.QTextEdit(self.splitter)
        self.results_evaluation.setObjectName(_fromUtf8("results_evaluation"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 8)
        self.tab_machine_translation.setAutoFillBackground(True)
        self.tab_machine_translation.setObjectName(_fromUtf8("tab_machine_translation"))

        #btnMachineTranslation
        self.btnMachineTranslation = QtGui.QPushButton(self.groupBox)
        self.btnMachineTranslation.setEnabled(True)
        self.btnMachineTranslation.setMinimumSize(QtCore.QSize(120, 30))
        self.btnMachineTranslation.setFlat(False)
        self.btnMachineTranslation.setObjectName(_fromUtf8("btnMachineTranslation"))
        self.gridLayout.addWidget(self.btnMachineTranslation, 4, 1, 1, 4)

        #BEGGINING OF tab_evaluation
        self.tab_evaluation = QtGui.QWidget()
        self.tab_evaluation.setAutoFillBackground(True)
        self.tab_evaluation.setObjectName(_fromUtf8("tab_evaluation"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_evaluation)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_evaluation = QtGui.QGroupBox(self.tab_evaluation)
        self.groupBox_evaluation.setObjectName(_fromUtf8("groupBox_evaluation"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_evaluation)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #label_source_evaluation_tab
        self.label_source_evaluation_tab = QtGui.QLabel(self.groupBox_evaluation)
        self.label_source_evaluation_tab.setObjectName(_fromUtf8("label_source_evaluation_tab"))
        self.gridLayout.addWidget(self.label_source_evaluation_tab, 1, 1, 1, 1)
        #btn_source_evaluation_tab
        self.btn_source_evaluation_tab = QtGui.QPushButton(self.groupBox_evaluation)
        self.btn_source_evaluation_tab.setObjectName(_fromUtf8("btn_source_evaluation_tab"))
        self.gridLayout.addWidget(self.btn_source_evaluation_tab, 1, 3, 1, 1)
        #edit_source_evaluation_tab
        self.edit_source_evaluation_tab = QtGui.QLineEdit(self.groupBox_evaluation)
        self.edit_source_evaluation_tab.setReadOnly(True)
        self.edit_source_evaluation_tab.setObjectName(_fromUtf8("edit_source_evaluation_tab"))
        self.gridLayout.addWidget(self.edit_source_evaluation_tab, 1, 2, 1, 1)

        #label_target_evaluation_tab
        self.label_target_evaluation_tab = QtGui.QLabel(self.groupBox_evaluation)
        self.label_target_evaluation_tab.setObjectName(_fromUtf8("label_target_evaluation_tab"))
        self.gridLayout.addWidget(self.label_target_evaluation_tab, 2, 1, 1, 1)
        #btn_target_evaluation_tab
        self.btn_target_evaluation_tab = QtGui.QPushButton(self.groupBox_evaluation)
        self.btn_target_evaluation_tab.setObjectName(_fromUtf8("btn_target_evaluation_tab"))
        self.gridLayout.addWidget(self.btn_target_evaluation_tab, 2, 3, 1, 1)
        #edit_target_evaluation_tab
        self.edit_target_evaluation_tab = QtGui.QLineEdit(self.groupBox_evaluation)
        self.edit_target_evaluation_tab.setReadOnly(True)
        self.edit_target_evaluation_tab.setObjectName(_fromUtf8("edit_target_evaluation_tab"))
        self.gridLayout.addWidget(self.edit_target_evaluation_tab, 2, 2, 1, 1)

        #label_output_dir_evaluation_tab
        self.label_output_dir_evaluation_tab = QtGui.QLabel(self.groupBox_evaluation)
        self.label_output_dir_evaluation_tab.setObjectName(_fromUtf8("label_output_dir_evaluation_tab"))
        self.gridLayout.addWidget(self.label_output_dir_evaluation_tab, 3, 1, 1, 1)
        #btn_output_dir_evaluation_tab
        self.btn_output_dir_evaluation_tab = QtGui.QPushButton(self.groupBox_evaluation)
        self.btn_output_dir_evaluation_tab.setObjectName(_fromUtf8("btn_output_dir_evaluation_tab"))
        self.gridLayout.addWidget(self.btn_output_dir_evaluation_tab, 3, 3, 1, 1)
        #edit_output_evaluation_tab
        self.edit_output_evaluation_tab = QtGui.QLineEdit(self.groupBox_evaluation)
        self.edit_output_evaluation_tab.setReadOnly(True)
        self.edit_output_evaluation_tab.setObjectName(_fromUtf8("edit_output_evaluation_tab"))
        self.gridLayout.addWidget(self.edit_output_evaluation_tab, 3, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.groupBox_evaluation)
        self.splitter = QtGui.QSplitter(self.tab_evaluation)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.results_preprocessing = QtGui.QTextEdit(self.splitter)
        self.results_preprocessing.setObjectName(_fromUtf8("results_preprocessing"))
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 8)
        self.tab_evaluation.setAutoFillBackground(True)
        self.tab_evaluation.setObjectName(_fromUtf8("tab_evaluation"))

        #btnEvaluation
        self.btnEvaluation = QtGui.QPushButton(self.groupBox_evaluation)
        self.btnEvaluation.setEnabled(True)
        self.btnEvaluation.setMinimumSize(QtCore.QSize(120, 30))
        self.btnEvaluation.setFlat(False)
        self.btnEvaluation.setObjectName(_fromUtf8("btnEvaluation"))
        self.gridLayout.addWidget(self.btnEvaluation, 4, 1, 1, 8)

        self.btn_check_WER = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_WER.setEnabled(True)
        self.btn_check_WER.setText("WER")
        self.btn_check_WER.setObjectName(_fromUtf8("btn_check_WER"))
        self.gridLayout.addWidget(self.btn_check_WER, 1, 5, 1, 1)

        self.btn_check_PER = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_PER.setEnabled(True)
        self.btn_check_PER.setText("PER")
        self.btn_check_PER.setObjectName(_fromUtf8("btn_check_PER"))
        self.gridLayout.addWidget(self.btn_check_PER, 1, 6, 1, 1)

        self.btn_check_HTER = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_HTER.setEnabled(True)
        self.btn_check_HTER.setText("HTER")
        self.btn_check_HTER.setObjectName(_fromUtf8("btn_check_HTER"))
        self.gridLayout.addWidget(self.btn_check_HTER, 1, 7, 1, 1)


        self.btn_check_GTM = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_GTM.setEnabled(True)
        self.btn_check_GTM.setText("GTM")
        self.btn_check_GTM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_GTM.setObjectName(_fromUtf8("btn_check_GTM"))
        self.gridLayout.addWidget(self.btn_check_GTM, 1, 8, 1, 1)


        self.btn_check_BLEU = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_BLEU.setEnabled(True)
        self.btn_check_BLEU.setText("BLEU")
        self.btn_check_BLEU.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU.setObjectName(_fromUtf8("btn_check_BLEU"))
        self.gridLayout.addWidget(self.btn_check_BLEU, 2, 5, 1, 1)

        self.btn_check_BLEU2GRAM = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_BLEU2GRAM.setEnabled(True)
        self.btn_check_BLEU2GRAM.setText("BLEU2")
        self.btn_check_BLEU2GRAM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU2GRAM.setObjectName(_fromUtf8("btn_check_BLEU2GRAM"))
        self.gridLayout.addWidget(self.btn_check_BLEU2GRAM, 2, 6, 1, 1)


        self.btn_check_BLEU3GRAM = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_BLEU3GRAM.setEnabled(True)
        self.btn_check_BLEU3GRAM.setText("BLEU3")
        self.btn_check_BLEU3GRAM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU3GRAM.setObjectName(_fromUtf8("btn_check_BLEU3GRAM"))
        self.gridLayout.addWidget(self.btn_check_BLEU3GRAM, 2, 7, 1, 1)


        self.btn_check_BLEU4GRAM = QtGui.QCheckBox(self.groupBox_evaluation)
        self.btn_check_BLEU4GRAM.setEnabled(True)
        self.btn_check_BLEU4GRAM.setText("BLEU4")
        self.btn_check_BLEU4GRAM.setMinimumSize(QtCore.QSize(5, 5))
        self.btn_check_BLEU4GRAM.setObjectName(_fromUtf8("btn_check_BLEU4GRAM"))
        self.gridLayout.addWidget(self.btn_check_BLEU4GRAM, 2, 8, 1, 1)

        self.label_evaluation_checkboxes_explanation = QtGui.QLabel(self.groupBox_evaluation)
        self.label_evaluation_checkboxes_explanation.setObjectName(_fromUtf8("label_evaluation_checkboxes_explanation"))
        self.label_evaluation_checkboxes_explanation.setText("*BLUE returns the average of all the BLUE tests,\n and BLUE2 means BLUE2GRAM")
        self.gridLayout.addWidget(self.label_evaluation_checkboxes_explanation, 3, 5, 1, 4)

        #BEGGINING OF tab_post_editing
        self.tab_post_editing = QtGui.QWidget()
        self.tab_post_editing.setAutoFillBackground(True)
        self.tab_post_editing.setObjectName(_fromUtf8("tab_post_editing"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_post_editing)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_post_editing)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #label_source_post_editing
        self.label_source_post_editing = QtGui.QLabel(self.groupBox)
        self.label_source_post_editing.setObjectName(_fromUtf8("label_source_post_editing"))
        self.gridLayout.addWidget(self.label_source_post_editing, 1, 1, 1, 1)
        #btn_source_post_editing
        self.btn_source_post_editing = QtGui.QPushButton(self.groupBox)
        self.btn_source_post_editing.setObjectName(_fromUtf8("btn_source_post_editing"))
        self.gridLayout.addWidget(self.btn_source_post_editing, 1, 3, 1, 1)
        #edit_source_post_editing
        self.edit_source_post_editing = QtGui.QLineEdit(self.groupBox)
        self.edit_source_post_editing.setReadOnly(True)
        self.edit_source_post_editing.setObjectName(_fromUtf8("edit_source_post_editing"))
        self.gridLayout.addWidget(self.edit_source_post_editing, 1, 2, 1, 1)

        #label_target_post_editing
        self.label_target_post_editing = QtGui.QLabel(self.groupBox)
        self.label_target_post_editing.setObjectName(_fromUtf8("label_target_post_editing"))
        self.gridLayout.addWidget(self.label_target_post_editing, 2, 1, 1, 1)
        #btn_target_post_editing
        self.btn_target_post_editing = QtGui.QPushButton(self.groupBox)
        self.btn_target_post_editing.setObjectName(_fromUtf8("btn_target_post_editing"))
        self.gridLayout.addWidget(self.btn_target_post_editing, 2, 3, 1, 1)
        #edit_target_post_editing
        self.edit_target_post_editing = QtGui.QLineEdit(self.groupBox)
        self.edit_target_post_editing.setReadOnly(True)
        self.edit_target_post_editing.setObjectName(_fromUtf8("edit_target_post_editing"))
        self.gridLayout.addWidget(self.edit_target_post_editing, 2, 2, 1, 1)

        self.verticalLayout_2.addWidget(self.groupBox)
        self.splitter = QtGui.QSplitter(self.tab_post_editing)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))

        self.splitter2 = QtGui.QSplitter(self.tab_post_editing)
        self.splitter2.setOrientation(QtCore.Qt.Vertical)
        self.splitter2.setObjectName(_fromUtf8("splitter2"))

        self.table_post_processing = MyTable({'col1':[], 'col2':[]},10,2)
        self.splitter.addWidget(self.table_post_processing)
        self.verticalLayout_2.addWidget(self.splitter)
        self.verticalLayout_2.setStretch(1, 8)
        self.tab_post_editing.setAutoFillBackground(True)
        self.tab_post_editing.setObjectName(_fromUtf8("tab_post_editing"))

        self.search_table_post_processing = MyTable({},10,2)
        self.splitter.addWidget(self.search_table_post_processing)
        self.verticalLayout_2.addWidget(self.splitter2)
        self.verticalLayout_2.setStretch(1, 8)
        self.tab_post_editing.setAutoFillBackground(True)
        self.tab_post_editing.setObjectName(_fromUtf8("tab_post_editing"))

        self.btnSearchPostEditing = QtGui.QPushButton(self.groupBox)
        self.btnSearchPostEditing.setEnabled(True)
        self.btnSearchPostEditing.setMinimumSize(QtCore.QSize(120, 30))
        self.btnSearchPostEditing.setFlat(False)
        self.btnSearchPostEditing.setObjectName(_fromUtf8("btnSearchPostEditing"))
        self.gridLayout.addWidget(self.btnSearchPostEditing, 4, 3, 1, 1)
        self.toggled_search_post_editing = True
        self.search_table_post_processing.hide()

        self.btnStartPostEditing = QtGui.QPushButton(self.groupBox)
        self.btnStartPostEditing.setEnabled(True)
        self.btnStartPostEditing.setMinimumSize(QtCore.QSize(120, 30))
        self.btnStartPostEditing.setFlat(False)
        self.btnStartPostEditing.setObjectName(_fromUtf8("btnStartPostEditing"))
        self.gridLayout.addWidget(self.btnStartPostEditing, 4, 1, 1, 2)
        self.toggled_table_post_processing = True
        self.table_post_processing.hide()





        self.tabWidget.addTab(self.tab_corpus_preparation, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_training, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_machine_translation, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_evaluation, _fromUtf8(""))
        self.tabWidget.addTab(self.tab_post_editing, _fromUtf8(""))


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

    def initialize_tab_evaluation(self):
        self.label_source_evaluation_tab.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.label_target_evaluation_tab.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.label_output_dir_evaluation_tab.setText(_translate("MainWindow", "Output text", None))
        self.btn_output_dir_evaluation_tab.setText(_translate("Dialog", "...", None))
        self.btnEvaluation.setText(_translate("MainWindow", "Start Evaluation", None))
        self.groupBox_evaluation.setTitle(_translate("MainWindow", "Evaluation", None))

    def initialize_tab_machine_translation(self):
        self.label_source_machine_translation_tab.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_machine_translation_tab.setText(_translate("Dialog", "...", None))
        self.label_target_machine_translation_tab.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_machine_translation_tab.setText(_translate("Dialog", "...", None))
        self.btnMachineTranslation.setText(_translate("MainWindow", "Start Machine Translation", None))

    def initialize_post_editing_tab(self):
        self.label_source_post_editing.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_post_editing.setText(_translate("Dialog", "...", None))
        self.label_target_post_editing.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_post_editing.setText(_translate("Dialog", "...", None))
        self.btnSearchPostEditing.setText(_translate("Dialog", "Search", None))
        self.btnStartPostEditing.setText(_translate("Dialog", "Start Post-Editing", None))

    def initialize_preprocessing_tab(self):
        self.label_source_preprocessing_tab.setText(_translate("MainWindow", "Source text", None))
        self.btn_source_preprocessing_tab.setText(_translate("Dialog", "...", None))
        self.label_target_preprocessing_tab.setText(_translate("MainWindow", "Target text", None))
        self.btn_target_preprocessing_tab.setText(_translate("Dialog", "...", None))
        self.label_output_dir_preprocessing_tab.setText(_translate("MainWindow", "Output Directory", None))
        self.btn_output_dir_preprocessing_tab.setText(_translate("Dialog", "...", None))
        self.btnPreProccess.setText(_translate("MainWindow", "Start corpus preprocessing", None))

    def initialize_training_tab(self):
        self.btnTraining.setText(_translate("MainWindow", "Start Training", None))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Translators Training Tool", None))
        self.initialize_tab_machine_translation()
        self.initialize_preprocessing_tab()
        self.initialize_training_tab()
        self.initialize_tab_evaluation()
        self.initialize_post_editing_tab()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_corpus_preparation), _translate("MainWindow", "Corpus Preparation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_training), _translate("MainWindow", "Training", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_evaluation), _translate("MainWindow", "Evaluation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_machine_translation), _translate("MainWindow", "Machine Translation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_post_editing), _translate("MainWindow", "Post Processing", None))
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
