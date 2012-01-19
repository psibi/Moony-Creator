#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_moony_mainwindow
import ui_formatdialog
import formatdialog
import moony_resource_rc

__version__ = "1.0.0"

class MoonyMainWindow(QMainWindow,ui_moony_mainwindow.Ui_MainWindow):
    def __init__(self,parent=None):
        super(MoonyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.actionStart_Formatting,SIGNAL("triggered()"),self.on_pushButton_clicked)
        self.connect(self.action_About_Moony_Creator,SIGNAL("triggered()"),self.helpAbout)
        self.connect(self.actionStop_Formatting,SIGNAL("triggered()"),self.stopFormat)
        self.connect(self.actionQuit,SIGNAL("triggered()"),self.close)
        settings = QSettings()
        size = settings.value("MainWindow/Size",QVariant(QSize(550,493))).toSize()
        self.resize(size)
        position = settings.value("MainWindow/Position",QVariant(QPoint(0, 0))).toPoint()
        self.move(position)
        self.restoreState(settings.value("MainWindow/State").toByteArray())
        
    @pyqtSignature("QString")
    def on_comboBox_currentIndexChanged(self,text):
        if (text=="ext2" or "ext3"):
            self.featuresVisible(True)
            self.feat2Label.setText("UUID")
            self.feat3Label.setText("Block Size")
            self.feat4Label.setText("Fragment Size")
            self.feat5Label.setText("Bytes per inode")
            if (text=="ext2"):
                self.fstypeLabel.setText("ext2")
            else:
                self.fstypeLabel.setText("ext3")

        if (text=="xfs"):
            self.featuresVisible(False)
            self.feat2Label.setText("Block Size:")
            self.feat3Label.setText("Sector Size:")
            self.fstypeLabel.setText("xfs")

        if (text=="vfat"):
            self.featuresVisible(True)
            self.feat1Label.setText("Label")
            self.feat2Label.setText("Volume-ID")
            self.feat3Label.setText("Fat Size")
            self.feat4Label.setText("Number of Fats")
            self.feat5Label.setText("Disk sectors per cluster")
            self.fstypeLabel.setText("vfat")

    def featuresVisible(self,show):
            self.feat4Label.setVisible(show)
            self.feat5Label.setVisible(show)
            self.feat4LineEdit.setVisible(show)
            self.feat5LineEdit.setVisible(show)

    @pyqtSignature("")
    def on_pushButton_clicked(self):
        format_dlg=formatdialog.formatDialog(self)
        fsdetails=(self.fstypeLabel.text(),self.comboBox_2.currentText(),self.feat1LineEdit.text(),self.feat2LineEdit.text(),self.feat3LineEdit.text(),self.feat4LineEdit.text(),self.feat5LineEdit.text())
        format_dlg.findfstype(fsdetails)
        self.pushButton.setEnabled(False)
        self.actionStart_Formatting.setEnabled(False)
        if format_dlg.formatokpushButton.isEnabled():
            self.pushButton.setEnabled(True)
            self.actionStart_Formatting.setEnabled(True)

    def stopFormat(self):
        if not self.pushButton.isEnabled():
            #If the formatting process is taking place
            QMessageBox.warning(self,"Sorry, Cannot be stopped","Formatting cannot be stopped.\n\nStopping it now may corrupt the filesystem.")
        else:
            QMessageBox.information(self,"Moony Converter Info","No formatting is taking place")
            
    def closeEvent(self,event):
        settings=QSettings()
        settings.setValue("MainWindow/Size", QVariant(self.size()))
        settings.setValue("MainWindow/Position",QVariant(self.pos()))
        settings.setValue("MainWindow/State",QVariant(self.saveState()))

    def helpAbout(self):
        QMessageBox.about(self,"About Moony Creator","""<b>Moony Creator</b> %s
                <p>Copyright &copy; 2011 Sibi,Rijvana Nasreen 
                All rights reserved.
                <p>This application can be used to format
                removable storage devices.""" %(__version__))
        
def main():                          
    import sys
    import time
    import os
    app=QApplication(sys.argv)
    current_user=os.getuid()
    if current_user !=0:
        QMessageBox.critical(None,"Root Privileges Required","Moony Creator requires root permission")
    else:
        app.setOrganizationName("Lime Softwares")
        app.setOrganizationDomain("sibi-linux.blogspot.com")
        app.setApplicationName("Moony Creator")
        splash_pix=QPixmap(":/images/images/splash.jpg")
        splash=QSplashScreen(splash_pix,Qt.WindowStaysOnTopHint)
        splash.setMask(splash_pix.mask())
        splash.show()
        time.sleep(2)
        form=MoonyMainWindow()
        form.show()
        splash.finish(form)
        app.exec_()

main()

