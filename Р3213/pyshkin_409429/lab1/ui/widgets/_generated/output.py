# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/widgets/_source/output.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(621, 696)
        self.output_text = QtWidgets.QPlainTextEdit(Form)
        self.output_text.setGeometry(QtCore.QRect(10, 10, 601, 681))
        self.output_text.setStyleSheet("")
        self.output_text.setReadOnly(True)
        self.output_text.setObjectName("output_text")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
