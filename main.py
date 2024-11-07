# Hi fellers
# ------------------------------ Version ------------------------------#
#Version 1.0.0
#Author nhiasi
import json
# ------------------------------ Import ------------------------------#
import sys
#from lib2to3.btm_utils import MinNode
import os
import time
import threading

from PyQt6.QtWidgets import QWidget
#from PyQt6.QtWidgets.QWidget import window
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow as ui

from PyQt6.QtCore import QTime, QTimer


# ------------------------------ Standarts ------------------------------#




# ------------------------------ Code ------------------------------#


def main_setup():
    if not MainFenster.textEdit.toPlainText():
        with open("PData/notiz.txt") as file:
            if file:
                MainFenster.textEdit.setText(file.read())

    todo = ToDo()
    todo.set_todos()

    # bisschen hard dirty bitte besser machen
    def chbo1():
        QTimer.singleShot(550, lambda: todo.eins())

    def chbo2():
        QTimer.singleShot(550, lambda: todo.zwei())

    def chbo3():
        QTimer.singleShot(550, lambda: todo.drei())


    ### Main Fenster ###
    MainFenster.lineEdit.editingFinished.connect(do_search)
    MainFenster.lineEdit.setFocus()

    MainFenster.pushButton.clicked.connect(go_new)
    MainFenster.pushButton_2.clicked.connect(brows_button)
    MainFenster.pushButton_3.clicked.connect(last_button)
    MainFenster.pushButton_4.clicked.connect(marked_button)

    MainFenster.checkBox.stateChanged.connect(chbo1)
    MainFenster.checkBox_2.stateChanged.connect(chbo2)
    MainFenster.checkBox_3.stateChanged.connect(chbo3)

    MainFenster.pushButton_5.clicked.connect(edit_save)


    MainFenster.textEdit.textChanged.connect(save_note)


    MainFenster.label.setText("")

    ### New Fenster ###

    MainFenster.pushButton_6.clicked.connect(go_home)
    MainFenster.checkBox_4.stateChanged.connect(show4)





def go_home():
    MainFenster.stackedWidget.setCurrentWidget(MainFenster.page)

def save_note():
    def saving_note():
        MainFenster.textEdit.blockSignals(True)
        time.sleep(60)
        note_inhalt = MainFenster.textEdit.toPlainText()
        MainFenster.textEdit.blockSignals(False)
        with open("PData/notiz.txt", "w") as file:
            file.write(note_inhalt)
    note_thread = threading.Thread(target=saving_note)
    note_thread.start()


def go_new():
    MainFenster.stackedWidget.setCurrentWidget(MainFenster.page_2)
    # so kann man fenster aufrufen
    MainFenster.checkBox_4.setVisible(False)
    MainFenster.lineEdit_2.setFocus()

def edit_save():

    file_name = MainFenster.lineEdit_2.text()

    with open(f"Data/Notes/{file_name}.txt", "w") as file:
        file.write(MainFenster.plainTextEdit_2.toPlainText())
        MainFenster.plainTextEdit_2.toPlainText()

    if MainFenster.checkBox_5.isChecked():
        with open("PData/todos.json") as file:
            datei = json.load(file)
            data = list(datei)
            data.append(file_name)

    go_home()








def show4():
    MainFenster.checkBox_4.setVisible(True)

def brows_button():
    pass


def last_button():
    pass

def marked_button():
    pass


def do_search():
    suchbegriff = MainFenster.lineEdit.text()
    if suchbegriff != "":
        pfad = f"./Data/{suchbegriff}"
        if os.path.exists(pfad):

                open_file(pfad)

        else:
            MainFenster.label.setText("Datei nicht Vorhanden")
            QTimer.singleShot(1000, lambda:MainFenster.label.clear())

def open_file(pfad):
    with open(pfad, "w") as file:
        inhalt = file.read()

    pass


class ToDo:
    def __init__(self):
        with open("PData/todos.json") as file:
            self.datei = json.load(file)


    def eins(self):
        if MainFenster.checkBox.isChecked():
            self.datei.pop(0)
            self.todo_done()
            self.set_todos()
            MainFenster.checkBox.setChecked(False)

    def zwei(self):
        if MainFenster.checkBox_2.isChecked():
            self.datei.pop(1)
            self.todo_done()
            self.set_todos()
            MainFenster.checkBox_2.setChecked(False)


    def drei(self):
        if MainFenster.checkBox_3.isChecked():
            self.datei.pop(2)
            self.todo_done()
            self.set_todos()
            MainFenster.checkBox_3.setChecked(False)



    def todo_done(self):
        with open("PData/todos.json", "w") as file:
            json.dump(self.datei, file)





    def set_todos(self):
        if len(self.datei) >= 3:
            MainFenster.checkBox.setText(self.datei[0])
            MainFenster.checkBox_2.setText(self.datei[1])
            MainFenster.checkBox_3.setText(self.datei[2])

        elif len(self.datei) == 2:
            MainFenster.checkBox.setVisible(True)
            MainFenster.checkBox_2.setVisible(True)
            MainFenster.checkBox_3.setVisible(False)

            MainFenster.checkBox.setText(self.datei[0])
            MainFenster.checkBox_2.setText(self.datei[1])

        elif len(self.datei) == 1:
            MainFenster.checkBox.setVisible(True)
            MainFenster.checkBox_2.setVisible(False)
            MainFenster.checkBox_3.setVisible(False)

            MainFenster.checkBox.setText(self.datei[0])

        elif len(self.datei) == 0:
            MainFenster.checkBox.setVisible(False)
            MainFenster.checkBox_2.setVisible(False)
            MainFenster.checkBox_3.setVisible(False)

# ------------------------------ Kontrolls ------------------------------#
app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
MainFenster = ui()
MainFenster.setupUi(window)

main_setup()
window.show()

sys.exit(app.exec())
