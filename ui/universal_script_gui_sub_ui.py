# Form implementation generated from reading ui file 'c:\Users\henrychen\Documents\gitlab\metisse\metisse\example\ui\universal_script_gui_sub.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(456, 537)
        self.stop_Button = QtWidgets.QPushButton(Dialog)
        self.stop_Button.setGeometry(QtCore.QRect(170, 460, 101, 51))
        self.stop_Button.setObjectName("stop_Button")
        self.record_label = QtWidgets.QLabel(Dialog)
        self.record_label.setGeometry(QtCore.QRect(30, 20, 221, 61))
        self.record_label.setObjectName("record_label")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(260, 30, 101, 41))
        self.lcdNumber.setDigitCount(6)
        self.lcdNumber.setObjectName("lcdNumber")
        self.log_label = QtWidgets.QLabel(Dialog)
        self.log_label.setGeometry(QtCore.QRect(70, 190, 321, 121))
        self.log_label.setObjectName("log_label")
        self.image_label = QtWidgets.QLabel(Dialog)
        self.image_label.setGeometry(QtCore.QRect(70, 310, 321, 141))
        self.image_label.setObjectName("image_label")
        self.info_label = QtWidgets.QLabel(Dialog)
        self.info_label.setGeometry(QtCore.QRect(70, 100, 301, 81))
        self.info_label.setObjectName("info_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.stop_Button.setText(_translate("Dialog", "中止"))
        self.record_label.setText(
            _translate(
                "Dialog",
                '<html><head/><body><p><span style=" font-size:36pt;">執行時間 :</span></p></body></html>',
            )
        )
        self.log_label.setText(_translate("Dialog", "TextLabel"))
        self.image_label.setText(_translate("Dialog", "TextLabel"))
        self.info_label.setText(_translate("Dialog", "TextLabel"))
