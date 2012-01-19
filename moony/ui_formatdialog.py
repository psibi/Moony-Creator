# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format_dialog.ui'
#
# Created: Tue Dec 21 16:12:59 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_formatDialog(object):
    def setupUi(self, formatDialog):
        formatDialog.setObjectName("formatDialog")
        formatDialog.setWindowModality(QtCore.Qt.NonModal)
        formatDialog.resize(422, 147)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/moon.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        formatDialog.setWindowIcon(icon)
        formatDialog.setModal(False)
        self.layoutWidget = QtGui.QWidget(formatDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 398, 130))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.moonLabel = QtGui.QLabel(self.layoutWidget)
        self.moonLabel.setText("")
        self.moonLabel.setPixmap(QtGui.QPixmap(":/images/images/fmoon.png"))
        self.moonLabel.setScaledContents(True)
        self.moonLabel.setWordWrap(False)
        self.moonLabel.setObjectName("moonLabel")
        self.horizontalLayout_4.addWidget(self.moonLabel)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.forfsLabel = QtGui.QLabel(self.layoutWidget)
        self.forfsLabel.setObjectName("forfsLabel")
        self.horizontalLayout.addWidget(self.forfsLabel)
        self.forfstype = QtGui.QLabel(self.layoutWidget)
        self.forfstype.setText("")
        self.forfstype.setObjectName("forfstype")
        self.horizontalLayout.addWidget(self.forfstype)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.percentageLabel = QtGui.QLabel(self.layoutWidget)
        self.percentageLabel.setObjectName("percentageLabel")
        self.horizontalLayout_2.addWidget(self.percentageLabel)
        spacerItem = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formatprogressBar = QtGui.QProgressBar(self.layoutWidget)
        self.formatprogressBar.setMaximum(10)
        self.formatprogressBar.setProperty("value", 0)
        self.formatprogressBar.setObjectName("formatprogressBar")
        self.verticalLayout.addWidget(self.formatprogressBar)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formatokpushButton = QtGui.QPushButton(self.layoutWidget)
        self.formatokpushButton.setEnabled(False)
        self.formatokpushButton.setObjectName("formatokpushButton")
        self.horizontalLayout_3.addWidget(self.formatokpushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.retranslateUi(formatDialog)
        QtCore.QObject.connect(self.formatokpushButton, QtCore.SIGNAL("clicked()"), formatDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(formatDialog)

    def retranslateUi(self, formatDialog):
        formatDialog.setWindowTitle(QtGui.QApplication.translate("formatDialog", "Formatting", None, QtGui.QApplication.UnicodeUTF8))
        self.forfsLabel.setText(QtGui.QApplication.translate("formatDialog", "FileSystem Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.percentageLabel.setText(QtGui.QApplication.translate("formatDialog", "Percentage Complete:", None, QtGui.QApplication.UnicodeUTF8))
        self.formatokpushButton.setText(QtGui.QApplication.translate("formatDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

import moony_resource_rc
