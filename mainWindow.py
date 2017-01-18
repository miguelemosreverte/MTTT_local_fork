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
from differences_module import Differences

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

        css = QtCore.QFile('./gui/pyqt.css')
        css.open(QtCore.QIODevice.ReadOnly)
        if css.isOpen():
           self.setStyleSheet(QtCore.QVariant(css.readAll()).toString())
        css.close()

        self.post_editing_data = {}
        self.differences_data = {}
        self.modified_references_indices =  []
        self.saved_modified_references = []
        self.unmodified_target = []
        self.modified_target = []
        self.last_changed_item_in_post_edition = None
        self.last_selected_search = None
        self.log = {}
        self.statistics = None
        self.differences = None
        shutil.rmtree("./statistics/generated", ignore_errors=True)
        os.makedirs("./statistics/generated")
        shutil.rmtree("./saved", ignore_errors=True)
        os.makedirs("./saved")
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

        if self.toggled_table_post_editing:
            self.toggled_table_post_editing= False
            self.table_post_editing.show()
        else:
            self.toggled_table_post_editing= True
            self.table_post_editing.hide()
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
    def on_edit_search_differences_textEdited(self,text):
        self.search_on_table_differences(text)

    @pyqtSignature("QString")
    def on_edit_search_post_editing_textEdited(self,text):
        self.search_on_table_post_editing(text)

    def update_table_PostEdition(self):
        start = self.table_offset_PostEdition
        end = self.table_offset_PostEdition + 10
        self.post_editing_data["source"] = self.source_text[start:end]
        self.post_editing_data["target"] = self.target_text[start:end]
        self.table_post_editing.setdata(self.post_editing_data)


    def update_table_Differences(self):
        '''
        start = self.table_offset_Differences
        end = self.table_offset_Differences + 10
        source_to_show = self.source_text[start:end]
        target_to_show = self.target_text[start:end]
        '''


        self.differences_data["source"] = self.enriched_target_text_original
        self.differences_data["target"] = self.enriched_target_text_modified
        self.table_differences.setdata(self.differences_data)

    def search_on_table_differences(self, text):
        self.search_table_differences.clear()
        text = str(text)
        self.search_buttons = []
        if self.differences_data["target"] and self.differences_data["source"]:
            column = 1
            for index,segment in enumerate(self.differences_data["target"]):
                row = index
                if text and text in segment:
                    self.search_buttons.append(QTextEdit())
                    tableItem = self.search_buttons[-1]
                    tableItem.setFixedWidth(250)
                    tableItem.setText(segment)
                    tableItem.setReadOnly(True)
                    tableItem.mousePressEvent = (lambda event= tableItem, tableItem= tableItem,x=row, y=column: self.show_selected_segment_from_search_differences(event, tableItem,x,y))
                    self.search_table_differences.setCellWidget(len(self.search_buttons)-1,0, tableItem)
    def search_on_table_post_editing(self, text):
        self.search_table_post_editing.clear()
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
                    tableItem.setReadOnly(True)
                    tableItem.mousePressEvent = (lambda event= tableItem, tableItem= tableItem,x=row, y=column: self.show_selected_segment_from_search_post_editing(event, tableItem,x,y))
                    self.search_table_post_editing.setCellWidget(len(self.search_buttons)-1,0, tableItem)

    @pyqtSignature("")
    def show_selected_segment_from_search_differences(self, event, tableItem, x, y):
        if self.last_selected_search is not None:
            self.changeQTextEditColor(self.last_selected_search, QColor( 255, 255, 255,255))
        self.last_selected_search = tableItem
        self.changeQTextEditColor(tableItem, QColor( 153, 255, 255,255))
        self.table_differences.scrollToItem(self.table_differences.item(x,y), QAbstractItemView.PositionAtCenter)
        self.table_differences.selectRow(x)
    @pyqtSignature("")
    def show_selected_segment_from_search_post_editing(self, event, tableItem, x, y):
        if self.last_selected_search is not None:
            self.changeQTextEditColor(self.last_selected_search, QColor( 255, 255, 255,255))
        self.last_selected_search = tableItem
        self.changeQTextEditColor(tableItem, QColor( 153, 255, 255,255))
        self.table_post_editing.scrollToItem(self.table_post_editing.item(x,y), QAbstractItemView.PositionAtCenter)
        self.table_post_editing.selectRow(x)

    @pyqtSignature("")
    def on_btnDiff_clicked(self):
        self.save();
        self.tabWidget.setTabEnabled(5,True)
        self.tabWidget.setCurrentIndex(5)
        self.get_modified_and_unmodified_target()
        if self.differences is None:
            self.differences = Differences(self.unmodified_target, self.modified_target)
        self.enriched_target_text_original,self.enriched_target_text_modified = self.differences.get_enriched_text()
        self.showDiffs()

    @pyqtSignature("")
    def on_btnStats_clicked(self):
        self.save();
        self.btnFirstStat.show()
        self.btnSecondStat.show()
        self.btnThirdStat.show()

    def load_log(self):
        log = {}
        log_filepath = os.path.abspath("./saved/" + "log.json")
        try:
            with open(log_filepath) as json_data:
                log = json.load(json_data)
        except:pass
        return log

    def get_latest_modifications (self):
        log = self.load_log()
        last_modifications = {}
        for a in sorted(log.keys()):
            for b in log[a]:
                last_modifications[b] = log[a][b]
        return last_modifications

    def get_modified_and_unmodified_target(self):
        self.unmodified_target = []
        self.modified_target = []
        with open(self.original_target_path) as fp:
            for line in fp:
                if line != '\n':
                    self.unmodified_target.append(line)
        latest_modifications = self.get_latest_modifications()
        for index, line in enumerate(self.unmodified_target):
            if str(index) in latest_modifications:
                self.modified_target.append(latest_modifications[str(index)])
            else:
                self.modified_target.append(line)

    @pyqtSignature("")
    def on_btnFirstStat_clicked(self):
        self.save_using_log()
        self.get_modified_and_unmodified_target()
        self.statistics = Statistics(self.unmodified_target, self.modified_target)
        self.statistics.calculate_statistics("time_per_segment")
        self.HTMLview.setUrl(QUrl("Statistics/generated/time_per_segment.html"));
        self.HTMLview.show()
        self.tabWidget.setTabEnabled(6,True)
        self.tabWidget.setCurrentIndex(6)

    @pyqtSignature("")
    def on_btnSecondStat_clicked(self):
        self.save_using_log()
        self.get_modified_and_unmodified_target()
        self.statistics = Statistics(self.unmodified_target, self.modified_target)
        self.statistics.calculate_statistics("insertions")
        self.HTMLview.setUrl(QUrl("Statistics/generated/insertions.html"));
        self.HTMLview.show()
        self.tabWidget.setTabEnabled(6,True)
        self.tabWidget.setCurrentIndex(6)

    @pyqtSignature("")
    def on_btnThirdStat_clicked(self):
        self.save_using_log()
        self.get_modified_and_unmodified_target()
        self.statistics = Statistics(self.unmodified_target, self.modified_target)
        self.statistics.calculate_statistics("deletions")
        self.HTMLview.setUrl(QUrl("Statistics/generated/deletions.html"));
        self.HTMLview.show()
        self.tabWidget.setTabEnabled(6,True)
        self.tabWidget.setCurrentIndex(6)

    def save(self):
        self.original_target_path = str(self.edit_target_post_editing.text())
        target_filename = self.original_target_path[self.original_target_path.rfind('/'):]
        text_file = open(str("./saved/" + target_filename), "w")
        text_file.write('\n'.join(self.target_text))
        text_file.close()
        self.save_using_log()

    @pyqtSignature("")
    def on_btnSave_clicked(self):
        self.save()
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
            self.search_table_post_editing.show()
            self.edit_search_post_editing.show()
        else:
            self.toggled_search_post_editing = True
            self.search_table_post_editing.hide()
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
        lm_text = self.edit_lm_text_preprocessing_tab.text()
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
            text = self.migrated_backend_main._prepare_corpus(output, source_language,target_language,source,target,lm_text)
            self.results_preprocessing.setText(text)

    @pyqtSignature("")
    def on_btn_source_evaluation_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.*)")
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
        dialog.setNameFilter("Choose a text target (*.*)")
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
    def on_btn_lm_text_preprocessing_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.*)")
        dialog.setViewMode(QFileDialog.Detail)
        if dialog.exec_():
            self.edit_lm_text_preprocessing_tab.setText(dialog.selectedFiles()[0])
    @pyqtSignature("")
    def on_btn_source_preprocessing_tab_clicked(self):
        """
        Slot documentation goes here.
        """
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("Choose a text source (*.*)")
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
        dialog.setNameFilter("Choose a text target (*.*)")
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
        if self.last_changed_item_in_post_edition is not None and self.last_changed_item_in_post_editionCoordinates not in self.modified_table_items_coordinates:
            self.changeQTextEditColor(self.last_changed_item_in_post_edition, QColor( 255, 255, 255,255))
        self.last_changed_item_in_post_edition = tableItem
        self.last_changed_item_in_post_editionCoordinates = (x,y)
        self.changeQTextEditColor(self.last_changed_item_in_post_edition, QColor( 153, 255, 255,255))

    def on_tableItemDifferencestextChanged(self, tableItem, x, y):
        pass
    def on_tableItemPostEditing_textChanged(self, tableItem, row_index,column_index):
        row_index += self.table_offset_PostEdition
        self.last_change_timestamp = int(time.time() * 1000)
        self.modified_table_items_coordinates.append((row_index,column_index))
        self.changeQTextEditColor(self.last_changed_item_in_post_edition, QColor( 51, 255, 153,255))
        self.btnStats.show()
        self.btnDiff.show()
        self.btnSave.show()
        self.target_text[row_index] = str(tableItem.toPlainText())
        if row_index not in self.modified_references_indices:
            self.modified_references_indices.append(row_index)

    def save_using_log(self):
        for modified_reference_index in self.modified_references_indices:
            modified_segment = self.target_text[modified_reference_index]
            self.saved_modified_references.append(modified_segment)
            if self.last_change_timestamp not in self.log:
                self.log[self.last_change_timestamp] = {}
            self.log[self.last_change_timestamp][modified_reference_index] = modified_segment
        with open("./saved/" + "log.json", 'w') as outfile:
            json.dump(self.log, outfile)

        self.modified_references_indices = []



    @pyqtSignature("QString")
    def on_labelInfo_linkActivated(self, link):
        """
        Slot documentation goes here.
        """
        dialog = DlgCredits(self)
        dialog.exec_()
