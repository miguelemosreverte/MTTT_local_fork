# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt4.QtCore import (
    pyqtSignature,
    QObject,
    Qt,
    SIGNAL,
    QUrl,
    )

#from PyQt4 import QtCore

from PyQt4.QtGui import (
    QMainWindow,
    QMessageBox,
    QProgressDialog,
    QDialog,
    QFileDialog,
    QTextEdit,
    QColor,
    QAbstractItemView,
    )
from PyQt4 import QtCore
import sys
import time
import threading
import shutil

from Ui_mainWindow import Ui_MainWindow
from addMTModel import AddMTModelDialog
from chooseMTModel import ChooseMTModelDialog
from engine import Engine
from credits import DlgCredits
from util import doAlert


from table import MyTable


from migrated_backend_main import *
from statistics_module import Statistics

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
        self.post_editing_data = {}
        self.differences_data = {}
        self.modified_references_indices =  []
        self.saved_modified_references = []
        self.log = {}
        self.statistics = None
        shutil.rmtree("./statistics/generated", ignore_errors=True)
        os.makedirs("./statistics/generated")
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
    def on_btnStartDifferences_clicked(self):
        self.table_offset_Differences = 0
        self.update_table_Differences()
        self.btnNextDifferences.show()
        self.btnBackDifferences.show()
    def showDiffs(self):
        self.table_offset_Differences = 0
        self.update_table_Differences()
        self.btnNextDifferences.show()
        self.btnBackDifferences.show()
        self.table_differences.show()

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
        self.source_text = []
        self.target_text = []
        with open(source) as fp:
                for line in fp:
                    #line = unicode(line, 'iso8859-15')
                    if line != '\n':
                       self.source_text.append(textwrap.fill(line,40))
        with open(target) as fp:
                for line in fp:
                    #line = unicode(line, 'iso8859-15')
                    if line != '\n':
                       self.target_text.append(textwrap.fill(line,40))
        self.post_editing_data["source"] = self.source_text
        self.post_editing_data["target"] = self.target_text
        self.table_offset_PostEdition = 0
        self.table_offset_Differences = 0
        self.update_table_PostEdition()
        self.btnNextPostEditing.show()
        self.btnBackPostEditing.show()

    @pyqtSignature("QString")
    def on_edit_search_post_editing_textEdited(self,text):
        self.search_on_table(text)

    def update_table_PostEdition(self):
        start = self.table_offset_PostEdition
        end = self.table_offset_PostEdition + 10
        self.post_editing_data["source"] = self.source_text[start:end]
        self.post_editing_data["target"] = self.target_text[start:end]
        self.table_post_processing.setdata(self.post_editing_data)

    def update_table_Differences(self):
        start = self.table_offset_Differences
        end = self.table_offset_Differences + 10
        self.differences_data["source"] = self.source_text[start:end]
        self.differences_data["target"] = self.target_text[start:end]
        self.table_differences.setdata(self.differences_data)

    def search_on_table(self, text):
        self.search_table_post_processing.clear()
        text = str(text)
        self.search_buttons = []
        if self.post_editing_data["target"] and self.post_editing_data["source"]:
            column = 1
            for index,segment in enumerate(self.post_editing_data["target"]):
                row = index
                if text and text in segment:
                    self.search_buttons.append(QTextEdit())
                    tableItem = self.search_buttons[-1]
                    tableItem.setFixedWidth(250)
                    tableItem.setText(segment)
                    tableItem.mousePressEvent = (lambda event= tableItem, tableItem= tableItem,x=row, y=column: self.show_selected_segment_from_search(event, tableItem,x,y))
                    self.search_table_post_processing.setCellWidget(len(self.search_buttons)-1,0, tableItem)

    @pyqtSignature("")
    def show_selected_segment_from_search(self, event, tableItem, x, y):
        self.table_post_processing.scrollToItem(self.table_post_processing.item(x,y), QAbstractItemView.PositionAtCenter)
        self.table_post_processing.selectRow(x)

    @pyqtSignature("")
    def on_btnDiff_clicked(self):
        self.tabWidget.setTabEnabled(5,True)
        self.tabWidget.setCurrentIndex(5)
        self.showDiffs()

    @pyqtSignature("")
    def on_btnStats_clicked(self):
        if self.statistics is None:
            self.statistics = Statistics(self.source_text, self.target_text)
        self.statistics.calculate_statistics("time_per_segment")
        self.HTMLview.setUrl(QUrl("Statistics/generated/time_per_segment.html"));
        #self.HTMLview.reload()
        self.HTMLview.show()
        self.tabWidget.setTabEnabled(6,True)
        self.tabWidget.setCurrentIndex(6)

    @pyqtSignature("")
    def on_btnSave_clicked(self):
        text_file = open(str(self.edit_target_post_editing.text()), "w")
        text_file.write('\n'.join(self.target_text))
        text_file.close()
        self.save_using_log()
        self.btnSave.hide()

    @pyqtSignature("")
    def on_btnNextPostEditing_clicked(self):
        self.table_offset_PostEdition += 1
        self.update_table_PostEdition()

    @pyqtSignature("")
    def on_btnBackPostEditing_clicked(self):
        self.table_offset_PostEdition -= 1
        if self.table_offset_PostEdition < 0: self.table_offset_PostEdition = 0
        self.update_table_PostEdition()

    @pyqtSignature("")
    def on_btnNextDifferences_clicked(self):
        self.table_offset_Differences += 1
        self.update_table_Differences()

    @pyqtSignature("")
    def on_btnBackDifferences_clicked(self):
        self.table_offset_Differences -= 1
        if self.table_offset_Differences < 0: self.table_offset_Differences = 0
        self.update_table_Differences()

    @pyqtSignature("")
    def on_btnSearchDifferences_clicked(self):
        if self.toggled_search_differences:
            self.toggled_search_differences = False
            self.search_table_differences.show()
            self.edit_search_differences.show()
        else:
            self.toggled_search_differences = True
            self.search_table_differences.hide()
            self.edit_search_differences.hide()

    @pyqtSignature("")
    def on_btnSearchPostEditing_clicked(self):
        if self.toggled_search_post_editing:
            self.toggled_search_post_editing = False
            self.search_table_post_processing.show()
            self.edit_search_post_editing.show()
        else:
            self.toggled_search_post_editing = True
            self.search_table_post_processing.hide()
            self.edit_search_post_editing.hide()

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

    def changeQTextEditColor(self, tableItem, color):
        p = tableItem.palette()
        p.setColor(tableItem.backgroundRole(), color)
        tableItem.setPalette(p)

    def on_tableItemDifferences_selected(self, event, tableItem, x, y):
        pass
    def on_tableItemPostEdition_selected(self, event, tableItem, x, y):
        if self.lastChangedTableItem is not None and self.lastChangedTableItemCoordinates not in self.modified_table_items_coordinates:
            self.changeQTextEditColor(self.lastChangedTableItem, QColor( 255, 255, 255,255))
        self.lastChangedTableItem = tableItem
        self.lastChangedTableItemCoordinates = (x,y)
        self.changeQTextEditColor(self.lastChangedTableItem, QColor( 153, 255, 255,255))

    def on_tableItemDifferencestextChanged(self, tableItem, x, y):
        pass
    def on_tableItemPostEditing_textChanged(self, tableItem, x, y):
        y += self.table_offset_PostEdition
        self.last_change_timestamp = int(time.time() * 1000)
        self.modified_table_items_coordinates.append((x,y))
        self.changeQTextEditColor(self.lastChangedTableItem, QColor( 51, 255, 153,255))
        self.btnStats.show()
        self.btnDiff.show()
        self.btnSave.show()
        self.target_text[x] = str(tableItem.toPlainText())
        if y not in self.modified_references_indices:
            self.modified_references_indices.append(y)

    def save_using_log(self):
        for index,modified_reference_index in enumerate(self.modified_references_indices):
            modified_segment = self.target_text[modified_reference_index]
            if modified_segment not in self.saved_modified_references:
                self.saved_modified_references.append(modified_segment)
                if self.last_change_timestamp not in self.log:
                    self.log[self.last_change_timestamp] = {}
                self.log[self.last_change_timestamp][index] = modified_segment
        with open("log.json", 'w') as outfile:
            json.dump(self.log, outfile)

    @pyqtSignature("QString")
    def on_labelInfo_linkActivated(self, link):
        """
        Slot documentation goes here.
        """
        dialog = DlgCredits(self)
        dialog.exec_()
