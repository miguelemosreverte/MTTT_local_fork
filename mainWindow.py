# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import (
    pyqtSignature,
    QObject,
    Qt,
    SIGNAL,
    )

#from PyQt4 import QtCore

from PyQt4.QtGui import (
    QMainWindow,
    QMessageBox,
    QProgressDialog,
    QDialog,
    QFileDialog,
    )
from PyQt4 import QtCore
import sys
import threading

from Ui_mainWindow import Ui_MainWindow
from addMTModel import AddMTModelDialog
from chooseMTModel import ChooseMTModelDialog
from engine import Engine
from credits import DlgCredits
from util import doAlert


from table import MyTable


from migrated_backend_main import *

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def setupUi(self, mainWindow):
        super(MainWindow, self).setupUi(mainWindow)

    def __init__(self, parent=None,  dm=None, moses=None, workdir=None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        '''
        css = QtCore.QFile('./gui/paper/gtk.css')
        css.open(QtCore.QIODevice.ReadOnly)
        if css.isOpen():
           self.setStyleSheet(QtCore.QVariant(css.readAll()).toString())
        css.close()
        '''

        self.datamodel = dm
        self.engine = None
        self.progress = None
        self.workdir = workdir
        self.migrated_backend_main = MyWindow()


    @pyqtSignature("")
    def on_btnMachineTranslation_clicked(self):
        import textwrap
        source = self.edit_source_machine_translation_tab.text()
        target = self.edit_target_machine_translation_tab.text()
        if not source:
            doAlert("Please choose a source text first.")
            return
        if not target:
            doAlert("Please choose a target text first.")
            return
        text = self.migrated_backend_main._machine_translation(source,target)
        self.results_machine_translation.setText(text)

    @pyqtSignature("")
    def on_btnStartPostEditing_clicked(self):
        import textwrap
        source = self.edit_source_post_editing.text()
        target = self.edit_target_post_editing.text()
        if not source:
            doAlert("Please choose a source text first.")
            return
        if not target:
            doAlert("Please choose a target text first.")
            return

        if self.toggled_table_post_processing:
            self.toggled_table_post_processing = False
            self.table_post_processing.show()
        else:
            self.toggled_table_post_processing = True
            self.table_post_processing.hide()
        source_text = []
        target_text = []
        data = {}
        with open(source) as fp:
                for line in fp:
                    #line = unicode(line, 'iso8859-15')
                    if line != '\n':
                       source_text.append(textwrap.fill(line,40))
        with open(target) as fp:
                for line in fp:
                    #line = unicode(line, 'iso8859-15')
                    if line != '\n':
                       target_text.append(textwrap.fill(line,40))
        data['source'] = source_text
        data['target'] = target_text
        self.table_post_processing.setdata(data)


    @pyqtSignature("")
    def on_btnSearchPostEditing_clicked(self):
        if self.toggled_search_post_editing:
            self.toggled_search_post_editing = False
            self.search_table_post_processing.show()
        else:
            self.toggled_search_post_editing = True
            self.search_table_post_processing.hide()

    @pyqtSignature("")
    def on_btnTraining_clicked(self):
        """
        Slot documentation goes here.
        """
        text = self.migrated_backend_main._train()
        self.results_training.setText(text)

    @pyqtSignature("")
    def on_btnEvaluation_clicked(self):
        """
        Slot documentation goes here.
        """
        source = self.edit_source_evaluation_tab.text()
        target = self.edit_target_evaluation_tab.text()
        output = self.edit_output_evaluation_tab.text()

        if not source:
            doAlert("Please choose a source text first.")
            return
        elif not target:
            doAlert("Please choose a target text first.")
            return
        elif not output:
            doAlert("Please choose an output directory first.")
            return

        checkbox_indexes = [False] * 8 #checkbox_indexes["WER","PER","HTER", "GTM", "BLEU","BLEU2GRAM","BLEU3GRAM"]
        checkbox_indexes[0] = self.btn_check_WER.isChecked()
        checkbox_indexes[1] = self.btn_check_PER.isChecked()
        checkbox_indexes[2] = self.btn_check_HTER.isChecked()
        checkbox_indexes[3] = self.btn_check_GTM.isChecked()
        checkbox_indexes[4] = self.btn_check_BLEU.isChecked()
        checkbox_indexes[5] = self.btn_check_BLEU2GRAM.isChecked()
        checkbox_indexes[6] = self.btn_check_BLEU3GRAM.isChecked()
        checkbox_indexes[7] = self.btn_check_BLEU4GRAM.isChecked()

        text = self.migrated_backend_main._evaluate(checkbox_indexes, source, target)
        print text
        self.results_evaluation.setText(text)

    @pyqtSignature("")
    def on_btnPreProccess_clicked(self):
        """
        Slot documentation goes here.
        """
        source = self.edit_source_preprocessing_tab.text()
        target = self.edit_target_preprocessing_tab.text()
        output = self.edit_output_preprocessing_tab.text()
        source_language = self.preprocessing_target_language
        target_language = self.preprocessing_target_language

        if not source:
            doAlert("Please choose a source text first.")
            return
        elif not target:
            doAlert("Please choose a target text first.")
            return
        elif not output:
            doAlert("Please choose an output directory first.")
            return
        elif not source_language:
            doAlert("Please choose an preprocessing_source_language directory first.")
            return
        elif not target_language:
            doAlert("Please choose an preprocessing_target_language directory first.")
            return
        else:
            text = self.migrated_backend_main._prepare_corpus(output, source_language,target_language,source,target)
            self.results_preprocessing.setText(text)

    @pyqtSignature("")
    def on_btn_source_evaluation_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.txt)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_source_evaluation_tab.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_target_evaluation_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text target (*.txt)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_target_evaluation_tab.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_output_dir_evaluation_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        self.edit_output_evaluation_tab.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

    @pyqtSignature("")
    def on_btn_source_machine_translation_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.*)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_source_machine_translation_tab.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_target_machine_translation_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.*)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_target_machine_translation_tab.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_source_post_editing_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.*)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_source_post_editing.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_target_post_editing_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.*)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_target_post_editing.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_source_preprocessing_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.txt)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_source_preprocessing_tab.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_target_preprocessing_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text target (*.txt)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_target_preprocessing_tab.setText(dialog.selectedFiles()[0])

    @pyqtSignature("")
    def on_btn_output_dir_preprocessing_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        self.edit_output_preprocessing_tab.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

    @pyqtSignature("")
    def on_btnTranslate_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.engine is None:
            doAlert("Please load MT model first.")
            return
        self.btnTranslate.setEnabled(False)
        self.editTrg.setText("")
        try:
            texts = str(self.editSrc.toPlainText().toUtf8()).split('\n')
            trans = []
            for text in texts:
                if text.strip() == "":
                    trans.append(text)
                else:
                    trans.append(
                        self.engine.translate(
                            text.replace('\r', ' ').strip()).decode('utf8'))
            self.editTrg.setText('\n'.join(trans))
        except Exception, e:
            print >> sys.stderr, str(e)
            doAlert("Translation failed!")
        self.btnTranslate.setEnabled(True)
        self.btnTranslate.setFocus()

    @pyqtSignature("QString")
    def on_labelInfo_linkActivated(self, link):
        """
        Slot documentation goes here.
        """
        dialog = DlgCredits(self)
        dialog.exec_()
