# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(460, 340))
        MainWindow.setMaximumSize(QtCore.QSize(460, 340))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 460, 340))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_2 = QtWidgets.QLabel(parent=self.page)
        self.label_2.setGeometry(QtCore.QRect(255, 120, 50, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.page)
        self.textEdit.setGeometry(QtCore.QRect(245, 145, 190, 160))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(125, 75, 60, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.page)
        self.pushButton.setGeometry(QtCore.QRect(35, 75, 60, 80))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(125, 175, 60, 80))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit.setGeometry(QtCore.QRect(25, 20, 170, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(parent=self.page)
        self.line.setGeometry(QtCore.QRect(220, 10, 5, 330))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=self.page)
        self.label.setGeometry(QtCore.QRect(25, 275, 170, 30))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(35, 175, 60, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox = QtWidgets.QGroupBox(parent=self.page)
        self.groupBox.setGeometry(QtCore.QRect(245, 20, 190, 90))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 150, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 60, 150, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 40, 150, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 290, 80, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 5, 35, 25))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.pushButton_6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../PData/bilder/arrow_back.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=self.page_2)
        self.checkBox_4.setGeometry(QtCore.QRect(330, 35, 101, 22))
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 35, 150, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.page_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 60, 420, 220))
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 30, 380, 175))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.checkBox_5 = QtWidgets.QCheckBox(parent=self.page_2)
        self.checkBox_5.setGeometry(QtCore.QRect(260, 35, 61, 22))
        self.checkBox_5.setObjectName("checkBox_5")
        self.label_3 = QtWidgets.QLabel(parent=self.page_2)
        self.label_3.setGeometry(QtCore.QRect(45, 35, 45, 20))
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.page_3)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 160, 80, 22))
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "hiasNote"))
        self.label_2.setText(_translate("MainWindow", "Note"))
        self.pushButton_2.setText(_translate("MainWindow", "Brows"))
        self.pushButton.setText(_translate("MainWindow", "New"))
        self.pushButton_4.setText(_translate("MainWindow", "Marked"))
        self.label.setText(_translate("MainWindow", "########################"))
        self.pushButton_3.setText(_translate("MainWindow", "Last"))
        self.groupBox.setTitle(_translate("MainWindow", "TODO"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_5.setText(_translate("MainWindow", "Save"))
        self.checkBox_4.setText(_translate("MainWindow", "only ToDo"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Notiz"))
        self.checkBox_5.setText(_translate("MainWindow", "ToDo"))
        self.label_3.setText(_translate("MainWindow", "Name:"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
