# Hi fellers
# ------------------------------ Version ------------------------------#
#Version 1.0.0
#Author nhiasi

# ------------------------------ Import ------------------------------#
# ---------- Imports from py ---------- #
import sys
import json
import os
import time
import threading

# ---------- Imports from QT ---------- #
from qtpy import QtWidgets
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QFileDialog

# ---------- Imports from GUI ---------- #
from ui.mainwindow import Ui_MainWindow as ui
from ui.editwindow import Ui_Form as edit_ui

# ------------------------------ Code ------------------------------#
class HiasNote:

    def __init__(self):
        self.offene_file = ""
        self.suchbegriff = ""



        self.app = QtWidgets.QApplication(sys.argv)

        self.window = QtWidgets.QMainWindow()
        self.MainFenster = ui()
        self.MainFenster.setupUi(self.window)

        self.edit_window = QtWidgets.QMainWindow()
        self.EditFenster = edit_ui()
        self.EditFenster.setupUi(self.edit_window)



        self.main_setup()
        self.window.show()
        # edit_window.show()

        sys.exit(self.app.exec())

    def main_setup(self):
        if not self.MainFenster.textEdit.toPlainText():
            with open("PData/notiz.txt") as file:
                if file:
                    self.MainFenster.textEdit.setText(file.read())
        #TODO umschreiben
        self.todo_inni()
        self.set_todos()



        def chbo1():
            self.MainFenster.checkBox.disconnect()
            QTimer.singleShot(550, lambda: (self.todo_done(todu_num=0),
                                            self.MainFenster.checkBox.stateChanged.connect(chbo1) ))

        def chbo2():
            self.MainFenster.checkBox_2.disconnect()
            QTimer.singleShot(550, lambda: (self.todo_done(todu_num=1),
                                            self.MainFenster.checkBox_2.stateChanged.connect(chbo2) ))

        def chbo3():
            self.MainFenster.checkBox_3.disconnect()
            QTimer.singleShot(550, lambda: (self.todo_done(todu_num=2),
                              self.MainFenster.checkBox_3.stateChanged.connect(chbo3) ))

        ### Main Fenster ###
        self.MainFenster.lineEdit.editingFinished.connect(self.do_search)
        self.MainFenster.lineEdit.setFocus()

        self.MainFenster.pushButton.clicked.connect(self.go_new)
        self.MainFenster.pushButton_2.clicked.connect(self.brows_button)
        self.MainFenster.pushButton_3.clicked.connect(self.last_button)
        self.MainFenster.pushButton_4.clicked.connect(self.marked_button)

        self.MainFenster.checkBox.stateChanged.connect(chbo1)
        self.MainFenster.checkBox_2.stateChanged.connect(chbo2)
        self.MainFenster.checkBox_3.stateChanged.connect(chbo3)

        self.MainFenster.pushButton_5.clicked.connect(self.save_new_file)



        self.MainFenster.label.setText("")

        ### New Fenster ###
        self.MainFenster.pushButton_6.clicked.connect(self.go_home)
        self.MainFenster.checkBox_5.stateChanged.connect(self.show4)
        self.MainFenster.textEdit.textChanged.connect(self.save_new_note)

        ### Edit Fenster ###
        self.EditFenster.pushButton.clicked.connect(self.go_home)
        self.EditFenster.pushButton_2.clicked.connect(self.save_edit)
        self.EditFenster.pushButton_3.clicked.connect(self.do_mark)
        self.EditFenster.pushButton_4.clicked.connect(self.del_note)


        #MainFenster.stackedWidget.setCurrentWidget(MainFenster.page_3)

    def save_edit(self):
        inhalt = self.EditFenster.textEdit.toPlainText()
        with open(f"Data/{self.offene_file}", "w") as file:
            file.write(inhalt)
        #self.go_home()

    def del_note(self):
        self.edit_window.close()
        os.remove(f"Data/{self.offene_file}")

        self.go_home()

    def go_home(self):
        if self.MainFenster.stackedWidget.currentIndex() == 1:
            self.MainFenster.checkBox_4.setChecked(False)
            self.MainFenster.checkBox_4.setChecked(False)
            self.MainFenster.checkBox_5.setChecked(False)
            self.MainFenster.lineEdit_2.clear()
            self.MainFenster.plainTextEdit_2.clear()
        elif self.MainFenster.stackedWidget.currentIndex() == 3:
            pass
        else:
            self.edit_window.close()
            self.window.raise_()
            self.window.activateWindow()

            self.MainFenster.lineEdit.clear()
        self.todo_inni()
        self.set_todos()

        self.MainFenster.stackedWidget.setCurrentWidget(self.MainFenster.page)

    def brows_button(self):
        datei_name, _ = QFileDialog.getOpenFileName( caption="Datei auswählen", directory="./Data")

        if datei_name:

            path = "./" + datei_name.split("/")[-2] + "/" + datei_name.split("/")[-1]
            self.open_file(path)

    def save_new_note(self):
        def saving_note():
            self.MainFenster.textEdit.blockSignals(True)
            time.sleep(60)
            note_inhalt = self.MainFenster.textEdit.toPlainText()
            self.MainFenster.textEdit.blockSignals(False)
            with open("PData/notiz.txt", "w") as file:
                file.write(note_inhalt)
        note_thread = threading.Thread(target=saving_note)
        note_thread.start()

    def go_new(self):
        self.MainFenster.stackedWidget.setCurrentWidget(self.MainFenster.page_2)
        # so kann man fenster aufrufen
        self.MainFenster.checkBox_4.setVisible(False)
        self.MainFenster.lineEdit_2.setFocus()

    def save_new_file(self):
        file_name = self.MainFenster.lineEdit_2.text() + ".nh"
        if not self.MainFenster.checkBox_4.isChecked():
            with open(f"Data/{file_name}", "w") as file:
                inhalt = self.MainFenster.plainTextEdit_2.toPlainText()
                file.write(inhalt)

        if self.MainFenster.checkBox_5.isChecked():
            with open("PData/todos.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []

            data.append(file_name)

            with open("PData/todos.json", 'w') as file:
                json.dump(data, file)

        self.go_home()

    def show4(self):
        if self.MainFenster.checkBox_4.isVisible():
            self.MainFenster.checkBox_4.setVisible(False)
            self.MainFenster.checkBox_4.setChecked(False)
        else:
            self.MainFenster.checkBox_4.setVisible(True)

    def last_button(self):
        with open("PData/last.txt",) as file:
                data = file.read()
        try:
            self.open_file(f"Data/{data}")
        except FileNotFoundError:
            self.datei_not_found()

    def marked_button(self):
        with open("PData/marked.json",) as file:
                data = json.load(file)
        if data:
            try:
                self.open_file(f"Data/{data[0]}")
            except FileNotFoundError:
                self.datei_not_found()
        else:
            self.datei_not_found()

    def do_search(self):
        self.suchbegriff = self.MainFenster.lineEdit.text()
        if self.suchbegriff != "":
            pfad = f"./Data/{self.suchbegriff}.nh"
            if os.path.exists(pfad):
                self.open_file(pfad)
                #TODO mach das man suchbegriff irgendwie nach ausen bringt

            else:
                self.datei_not_found()

    def datei_not_found(self):
        self.MainFenster.label.setText("Datei nicht Vorhanden")
        QTimer.singleShot(1000, lambda: self.MainFenster.label.clear())

    def open_file(self, pfad):
        self.offene_file = os.path.basename(pfad)
        with open("PData/last.txt", "w") as file:
            file.write(self.offene_file)

        with open("PData/marked.json", "r") as file:
            datei = json.load(file)

            if self.offene_file in datei:
                self.EditFenster.pushButton_3.setText("Demakieren")
            else:
                self.EditFenster.pushButton_3.setText("Makieren")

        with open(pfad, 'r') as file:
            inhalt = file.read()

        self.EditFenster.label.setText(self.offene_file.partition(".")[0])
        self.EditFenster.textEdit.setText(inhalt)
        self.edit_window.show()

        self.MainFenster.lineEdit_2.clear()

    def do_mark(self):
        # kann man evtl auch so machen das man mehrere datein makieren kann
        # wird vorerst ausgeslassen

        with open("PData/marked.json", "r") as file:
            datei = json.load(file)

        if self.offene_file in datei:
            datei.remove(self.offene_file)
            self.EditFenster.pushButton_3.setText("Makieren")
        else:
            datei = [self.offene_file]
            self.EditFenster.pushButton_3.setText("Demakieren")
        with open("PData/marked.json", "w") as file:
            json.dump(datei, file)

    def todo_inni(self):
        with open("PData/todos.json") as file:
            try:
                self.datei = json.load(file)
            except json.JSONDecodeError:
                self.datei = []


    def todo_done(self, todu_num):
        chbo_list = [self.MainFenster.checkBox, self.MainFenster.checkBox_2, self.MainFenster.checkBox_3]
        del_file = f"Data/{self.datei[todu_num]}"

        if os.path.exists(del_file):
            os.remove(del_file)

        self.datei.pop(todu_num)
        with open("PData/todos.json", "w") as file:
            json.dump(self.datei, file)

        self.set_todos()
        chbo_list[todu_num].setCheckState(Qt.CheckState.Unchecked)


    def set_todos(self):
        if len(self.datei) >= 3:
            self.MainFenster.checkBox.setText(self.datei[0].partition(".")[0])
            self.MainFenster.checkBox_2.setText(self.datei[1].partition(".")[0])
            self.MainFenster.checkBox_3.setText(self.datei[2].partition(".")[0])
            self.MainFenster.checkBox.setVisible(True)
            self.MainFenster.checkBox_2.setVisible(True)
            self.MainFenster.checkBox_3.setVisible(True)

        elif len(self.datei) == 2:
            self.MainFenster.checkBox.setVisible(True)
            self.MainFenster.checkBox_2.setVisible(True)
            self.MainFenster.checkBox_3.setVisible(False)

            self.MainFenster.checkBox.setText(self.datei[0].partition(".")[0])
            self.MainFenster.checkBox_2.setText(self.datei[1].partition(".")[0])

        elif len(self.datei) == 1:
            self.MainFenster.checkBox.setVisible(True)
            self.MainFenster.checkBox_2.setVisible(False)
            self.MainFenster.checkBox_3.setVisible(False)

            self.MainFenster.checkBox.setText(self.datei[0].partition(".")[0])

        elif len(self.datei) == 0:
            self.MainFenster.checkBox.setVisible(False)
            self.MainFenster.checkBox_2.setVisible(False)
            self.MainFenster.checkBox_3.setVisible(False)


# ------------------------------ ExeQ ------------------------------#
if __name__ == "__main__":

    main = HiasNote()
    main.main_setup()