# Hi fellers
# ------------------------------ Version ------------------------------#
#Version 1.0.0

# ------------------------------ Import ------------------------------#
import sys
#from lib2to3.btm_utils import MinNode
import os
import time
import threading

from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow as ui
from PyQt6.QtCore import QTime, QTimer


# ------------------------------ Standarts ------------------------------#






# ------------------------------ Code ------------------------------#

def save_note():
    a = MainFenster.textEdit.toPlainText()
    print(a)

def new_button():
    pass
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
            with open(pfad, "w") as file:
                inhalt = file.read()

        else:
            def error_datei_nicht_gefunden():
                MainFenster.label.setText("Datei nicht Vorhanden")
                time.sleep(5)
                MainFenster.label.clear()
            timer_thread = threading.Thread(target=error_datei_nicht_gefunden)
            timer_thread.start()

def open_file():
    pass




class chbo():
    def eins(self):
        print("chbo1")
    def zwei(self):
        print("chbo2")
    def drei(self):
        print("chbo3")
# ------------------------------ Kontrolls ------------------------------#
app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
MainFenster = ui()



MainFenster.setupUi(window)


MainFenster.lineEdit.editingFinished.connect(do_search)

MainFenster.pushButton.clicked.connect(new_button)
MainFenster.pushButton_2.clicked.connect(brows_button)
MainFenster.pushButton_3.clicked.connect(last_button)
MainFenster.pushButton_4.clicked.connect(marked_button)

MainFenster.checkBox.stateChanged.connect(chbo.eins)
MainFenster.checkBox_2.stateChanged.connect(chbo.zwei)
MainFenster.checkBox_3.stateChanged.connect(chbo.drei)

#MainFenster.textEdit..connect(save_note)



#################### System ####################


window.show()
sys.exit(app.exec())
#################### END ####################